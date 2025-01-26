import praw

def authenticate():
    reddit = praw.Reddit(
        client_id="i6w_88G0jjFOoJPR0Ar9fg",
        client_secret="j0ILwFhscNDAYj0edRY9XUGge_zThg",
        username="Long_Humor167",
        password="prajwal2003",
        user_agent="RedditBot v1.0 (by u/Long_Humor167)"
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
