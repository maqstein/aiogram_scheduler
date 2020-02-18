SET timezone = 'Europe/Moscow';
DROP TABLE IF EXISTS query;
CREATE TABLE query(
    pr_id SERIAL PRIMARY KEY,
    user_id int,
    send_time timestamptz NOT NULL DEFAULT NOW()
);
DROP TABLE IF EXISTS chat_users;
CREATE TABLE chat_users(
    user_id int PRIMARY KEY,
    username text
)