relational database

backfill:
- fill data for previous days
 - for example: data was saved to mongodb on 11/10, but mysql was created 11/19, but I want to
 backfill this 11/10 data into mysql, this process of loading previous date data is called a backfill
 - backfill usually runs manually

- sentiment
    - post_id (mongobd default id + order)
    - DateGenerated: date (when this record was generated - mongobd: date)
    - DateInserted: timestamp: (when this record was inserted into mysql)

- redditTopic
 - subreddit id (int)
 - subreddit_name (varchar)