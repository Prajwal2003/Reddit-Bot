import praw


reddit = praw.Reddit(
        client_id="i6w_88G0jjFOoJPR0Ar9fg",
        client_secret="j0ILwFhscNDAYj0edRY9XUGge_zThg",
        username="Long_Humor167",
        password="prajwal2003",
        user_agent="RedditBot v1.0 (by u/Long_Humor167)"
)
print(reddit.auth.scopes())  # Check the granted OAuth scopes
