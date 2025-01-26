import praw

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

def post_and_comment(reddit):
    try:
        subreddit = reddit.subreddit("test")
        post = subreddit.submit("Hello Reddit!", selftext="This is a test post.")
        print(f"Posted to r/test: {post.title}")
        
        try:
            comment = post.reply("This is a test comment.")
            print("Commented successfully!")
        except Exception as e:
            print(f"Error commenting on post: {e}")

        try:
            post.upvote()
            print("Upvoted successfully!")
        except Exception as e:
            print(f"Error upvoting item: {e}")

    except Exception as e:
        print(f"Error posting to subreddit: {e}")

if __name__ == "__main__":
    reddit = authenticate()
    post_and_comment(reddit)
