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