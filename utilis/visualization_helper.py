import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import plotly.express as px

import sys
import os
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)


def gpt_sentiment_table(news_output_csv_path, post_output_csv_path):
    '''
    gpt_sentiment_table: return gpt_sentiment tabl
    gpt_sentiment_table: Str Str -> pd.DataFrame
    '''
    df_post = pd.read_csv(post_output_csv_path)
    df_news = pd.read_csv(news_output_csv_path)
    gpt_post = df_post[df_post['subreddit_id'] == 1]
    gpt_news = df_news[df_news['subreddit_id'] == 1]
    avg_news_per_day = gpt_news.groupby('date_generated').agg({'polarity': 'mean'}).reset_index()

    # load dataset for sentiment analysis
    gpt_sentiment = gpt_post.merge(avg_news_per_day, on = 'date_generated', how = 'left')[['post_id', 'date_generated', 'title', 'subjectivity', 'polarity_y', 'polarity_x']]
    gpt_sentiment.rename(columns = {'subjectivity':'subjectivity_post','polarity_y':'avg_polarity_news', 'polarity_x':'polarity_post'}, inplace = True)
    gpt_sentiment['title_length'] = gpt_sentiment['title'].apply(len)
    gpt_sentiment['post_sentiment_class'] = np.where(
        (gpt_sentiment['polarity_post'] > 0.5) & (gpt_sentiment['polarity_post'] <= 1), 'very positive',
        np.where(
            (gpt_sentiment['polarity_post'] <= 0.5) & (gpt_sentiment['polarity_post'] > 0), 'positive',
            np.where(
                gpt_sentiment['polarity_post'] == 0, 'neutral',
                np.where(
                    (gpt_sentiment['polarity_post'] >= -0.5) & (gpt_sentiment['polarity_post'] < 0), 'negative', 'very negative'
                )
            )
        )
    )
    gpt_sentiment = gpt_sentiment[['post_id', 'date_generated', 'title', 'title_length', 'subjectivity_post', 'avg_polarity_news', 'polarity_post', 'post_sentiment_class' ]]
    return gpt_sentiment



# draw Joint Plot - Subjectivity vs Polarity
def subjectivity_polarity_joint_plot(table, image_folder_path, image_filename):
    '''
    create joint plot to investigate the relation between post subjectivity and post polarity and save image to image_folder_path
    '''
    sns.set_theme(style="whitegrid")
    joint_plot = sns.jointplot(data=table, 
                            x='subjectivity_post', 
                            y='polarity_post', 
                            kind='hex', 
                            color='#d5bdaf', 
                            space=0, 
                            gridsize=16,
                            mincnt=1,
                            vmax=10,
                            marginal_kws=dict(bins=10, fill=True, color = '#d6ccc2'))

    # adding title and axis labels
    joint_plot.fig.suptitle('Reddit Post Subjectivity vs Polarity')
    joint_plot.set_axis_labels('Subjectivity', 'Polarity', fontsize=12)

    # prevent cutoffs
    joint_plot.fig.subplots_adjust(top=0.95)

    full_path = os.path.join(image_folder_path, image_filename)

    # Save the figure
    plt.savefig(full_path, dpi=300)
    plt.close(joint_plot.fig)




def news_post_polarity_point_plot(table, image_folder_path, image_filename):
    '''
    create point plot to correlate news polarity with post polarity and save image to image_folder_path
    '''
    # Create DataFrames from the two tables
    posts_polarity =  pd.DataFrame({'date':table['date_generated'], 'polarity': table['polarity_post'], 'type': 'Posts'})
    news_polarity =  pd.DataFrame({'date':table['date_generated'], 'polarity': table['avg_polarity_news'], 'type': 'News'})

    # Combine the DataFrames
    polarity_combined = pd.concat([news_polarity, posts_polarity ])

    # Make sure that there are indeed two types 'Posts' and 'News'
    assert polarity_combined['type'].nunique() == 2, "There should be exactly two types: 'Posts' and 'News'"

    # Create a point plot
    plt.figure(figsize=(8, 6))
    news_color = '#a2d2ff'
    post_color = "#ffafcc"
    point_plot = sns.pointplot(data=polarity_combined, x='date', y='polarity', hue='type', palette = [post_color, news_color])

    # Improve the aesthetics
    plt.xticks(rotation=45)
    plt.title('Comparison of News and Reddit Post Polarity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Polarity')
    plt.tight_layout()  # Adjust layout to fit the date labels

    full_path = os.path.join(image_folder_path, image_filename)
    
    # Save the figure
    point_plot.figure.savefig(full_path, dpi=300)
    plt.close(point_plot.figure)




# --------------------Plotting the distribution of title lengths--------------------

def distribution_title_length(table, image_folder_path, image_filename):
    '''
    create a box plot to visualize the distribution of title length and save image to image_folder_path
    '''
    # Set the aesthetic style of the plots
    sns.set_style('whitegrid')

    # Create the box plot
    box_plot = sns.boxplot(y='title_length', data=table)

    # Add title and labels
    plt.title('Box plot of Title Lengths in GPT Sentiment')
    plt.ylabel('Length of Title')

    full_path = os.path.join(image_folder_path, image_filename)
    
    # Save the figure
    box_plot.figure.savefig(full_path, dpi=300)
    plt.close(box_plot.figure)



# --------------------Plotting the distribution of sentiment class--------------------

def distribution_sentiment_class_countplot(table, color_pal, image_folder_path, image_filename):
    '''
    create count plot to investigate distribution of each post sentiment class and save image to image_folder_path
    '''
    # Set the aesthetic style of the plots
    sns.set_style('whitegrid')

    # Since we want to assign colors manually to each x category, we'll use 'hue'
    # First, create a copy to avoid modifying the original dataframe
    table_with_hue = table.copy()
    table_with_hue['hue'] = table_with_hue['post_sentiment_class']

    # Create the bar plot
    count_plot = sns.countplot(x='post_sentiment_class', hue='hue', data=table_with_hue, 
                               palette=color_pal, dodge=False)

    # Add title and labels 
    plt.title('Distribution of Post Sentiment Classes')
    plt.xlabel('Sentiment Class')
    plt.ylabel('Count')

    full_path = os.path.join(image_folder_path, image_filename)
    count_plot.figure.savefig(full_path, dpi=300)
    plt.close(count_plot.figure)

color_palette = {
        "very negative": "#d32e05",  
        "negative": "#f87a63",      
        "neutral": "#f2e8cf",      
        "positive": "#bcd379",     
        "very positive": "#326e2f"  
    }


# --------------------Plotting the Pie chart of the percentage of each sentiment class--------------------


def sentiment_pie_chart(table, color_pal, image_folder_path, image_filename):
    '''
    create a pie chart to depict the percentage of each sentiment class and save image to image_folder_path
    '''
    fig = px.pie(table, names='post_sentiment_class', title='Pie chart of each sentiment class',
                 color='post_sentiment_class', color_discrete_map=color_pal)
    

    full_path = os.path.join(image_folder_path, image_filename)
    
    fig.write_image(full_path, scale=2)  



