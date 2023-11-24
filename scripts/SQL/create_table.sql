CREATE TABLE RedditTopic (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subreddit_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE PostSentiment (
    post_id VARCHAR(255) PRIMARY KEY,
    subreddit_id INT,
    FOREIGN KEY (subreddit_id) REFERENCES RedditTopic(id),
    date_generated DATE,
    date_inserted TIMESTAMP,
    title VARCHAR(255),
    subjectivity FLOAT CHECK (subjectivity >= -1 AND subjectivity <= 1),
    polarity FLOAT CHECK (polarity >= -1 AND polarity <= 1)
);


