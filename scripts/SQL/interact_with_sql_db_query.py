## update data in RedditTopic
# check_insert_query = """
# IF NOT EXISTS (SELECT 1 FROM reddit_thread_analysis.RedditTopic WHERE subreddit_name = '{}' )
# BEGIN 
#     INSERT INTO reddit_thread_analysis.RedditTopic (subreddit_name) 
#     VALUES ({})
# END
# """

## update data in RedditTopic
check_insert_query ="""
INSERT INTO {}.RedditTopic (subreddit_name)
SELECT * FROM (SELECT '{}' AS subreddit_name) AS tmp
WHERE NOT EXISTS (
    SELECT 1 FROM {}.RedditTopic WHERE subreddit_name = '{}'
) LIMIT 1;
"""

## get id of subreddit_name
get_id = """
SELECT id,subreddit_name
FROM {}.RedditTopic
WHERE subreddit_name = '{}'
"""

## insert post data into PostSentiment
insert_post_data = """
INSERT INTO {}.PostSentiment (post_id, subreddit_id, date_generated, date_inserted, title, subjectivity, polarity) VALUES ('{}', '{}','{}','{}', '{}', '{}', '{}')
"""

## insert news data into NewsSentiment
insert_news_data = """
INSERT INTO {}.NewsSentiment (news_id, subreddit_id, date_generated, date_inserted, polarity) VALUES (%s, %s,%s,%s, %s)
"""

# get post id from PostSentiment
get_post_id = """
SELECT post_id
FROM {}.PostSentiment
WHERE post_id = '{}';
"""

# get news id from NewsSentiment
get_news_id = """
SELECT post_id
FROM {}.NewsSentiment
WHERE post_id = '{}';
"""


