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
INSERT INTO reddit_thread_analysis.RedditTopic (subreddit_name)
SELECT * FROM (SELECT '{}' AS subreddit_name) AS tmp
WHERE NOT EXISTS (
    SELECT 1 FROM reddit_thread_analysis.RedditTopic WHERE subreddit_name = '{}'
) LIMIT 1;
"""

## get id of subreddit_name
get_id = """
SELECT id,subreddit_name
FROM reddit_thread_analysis.RedditTopic
WHERE subreddit_name = '{}'
"""

## insert post data into PostSentiment
insert_post_data = """
INSERT INTO testing.PostSentiment (post_id, subreddit_id, date_generated, date_inserted, title)
SELECT * FROM (SELECT %s AS post_id, %s AS subreddit_id, %s AS date_generated, %s AS date_inserted, %s AS title) AS tmp
WHERE NOT EXISTS (
    SELECT 1 FROM testing.PostSentiment
    WHERE post_id = %s AND subreddit_id = %s AND date_generated = %s AND date_inserted = %s AND title = %s
)
LIMIT 1;
"""
# get post id from PostSentiment
get_post_id = """
SELECT post_id
FROM testing.PostSentiment
WHERE post_id = '{}';
"""


