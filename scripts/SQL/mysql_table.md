relational database

backfill:
- fill data for previous days
 - for example: data was saved to mongodb on 11/10, but mysql was created 11/19, but I want to
 backfill this 11/10 data into mysql, this process of loading previous date data is called a backfill
 - backfill usually runs manually

 - to be implemented:
  - backfill dag to backfill info for previous days inside mongodb

- Postsentiment
    - post_id (mongobd default id + order, varchar, unique, primary_key)
    - subreddit_id (foreign key, int)
    - date_generated: date (when this record was generated - mongobd: date)
    - date_inserted: timestamp: (when this record was inserted into mysql)
    - title (varchar)
    - Subjectivity (float)
    - Polarity (processed based on reddit post title, float)
        - textblob



- redditTopic
 - subreddit id (int)
 - subreddit_name (varchar)