import sys
import os
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)
from utilis.visualization_helper import *




def run_create_charts():
    news_output_csv_path = project_folder_path + '/output/posts_output.csv'
    post_output_csv_path = project_folder_path + '/output/news_output.csv'
    gpt_sentiment = gpt_sentiment_table(post_output_csv_path, news_output_csv_path)

    image_folder_path = os.path.join(project_folder_path, 'image')

    image_filename_1 = "Subjectivity_vs_Polarity_joint_plot.png"
    subjectivity_polarity_joint_plot(gpt_sentiment, image_folder_path, image_filename_1)

    image_filename_2 = "news_polarity_vs_post_polarity_point_plot.png"
    news_post_polarity_point_plot(gpt_sentiment, image_folder_path, image_filename_2)

    image_filename_3 = "title_length_boxplot.png"
    distribution_title_length(gpt_sentiment, image_folder_path, image_filename_3)

    color_palette = {
        "very negative": "#d32e05",  
        "negative": "#f87a63",      
        "neutral": "#f2e8cf",      
        "positive": "#bcd379",     
        "very positive": "#326e2f"  
    }
    image_filename_4 = "sentiment_class_countplot.png"
    distribution_sentiment_class_countplot(gpt_sentiment, color_palette, image_folder_path, image_filename_4)

    image_filename_5 = "sentiment_class_pie_chart.png"
    sentiment_pie_chart(gpt_sentiment, color_palette, image_folder_path, image_filename_5)