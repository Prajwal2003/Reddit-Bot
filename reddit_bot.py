import praw
import time
import random

def authenticate():
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        user_agent="RedditBot v1.0 (by u/YOUR_USERNAME)"
    )
    print(f"Authenticated as: {reddit.user.me()}")
    return reddit

def post_to_subreddit(reddit, subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        print(f"Posted to r/{subreddit_name}: {title}")
    except Exception as e:
        print(f"Error posting to r/{subreddit_name}: {e}")

def comment_on_post(reddit, post_url, comment_text):
    try:
        submission = reddit.submission(url=post_url)
        submission.reply(comment_text)
        print(f"Commented on post: {post_url}")
    except Exception as e:
        print(f"Error commenting on post: {e}")

def upvote_item(reddit, item_url):
    try:
        item = reddit.submission(url=item_url) if "comments" in item_url else reddit.comment(url=item_url)
        item.upvote()
        print(f"Upvoted: {item_url}")
    except Exception as e:
        print(f"Error upvoting item: {e}")

if __name__ == "__main__":
    reddit = authenticate()

    post_to_subreddit(reddit, "test", "Hello Reddit!", "This is an automated post.")
    time.sleep(random.randint(5, 10))

    comment_on_post(reddit, "https://www.reddit.com/r/test/comments/example", "Nice post!")
    time.sleep(random.randint(5, 10))

    upvote_item(reddit, "https://www.reddit.com/r/test/comments/example")
