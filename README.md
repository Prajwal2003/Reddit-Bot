# Reddit-Bot

This project is a Python-based Reddit bot that uses the [PRAW](https://praw.readthedocs.io/) library to interact with the Reddit API. The bot can:

1. Post content to a subreddit.
2. Comment on posts.
3. Upvote posts.
4. Send Direct Messages (DMs) to specified Reddit users.

---

## Features

### 1. Post and Comment
- Automatically creates a post in a specified subreddit.
- Replies to the created post with a comment.

### 2. Upvote Posts
- Upvotes a specific post after creation.

### 3. Send Direct Messages (DMs)
- Asks for a list of Reddit usernames and sends a personalized DM to each user.

---

## Prerequisites

1. **Python**: Ensure Python 3.7 or later is installed on your system.
2. **PRAW Library**: Install the Python Reddit API Wrapper:
   ```bash
   pip install praw
   ```
3. **Reddit Developer Account**: Create a Reddit app to get your client ID, client secret, and user agent.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/reddit-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd reddit-bot
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install praw
   ```

---

## Configuration

1. Create a Reddit app:
   - Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
   - Click "Create App" or "Create Another App."
   - Choose "script" as the app type.
   - Note down the **client ID**, **client secret**, and **redirect URI**.

2. Update the `authenticate` function in `reddit_bot.py`:
   ```python
   reddit = praw.Reddit(
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
       username="YOUR_USERNAME",
       password="YOUR_PASSWORD",
       user_agent="RedditBot v1.0 (by u/YOUR_USERNAME)"
   )
   ```

---

## Usage

### Run the Bot
Execute the script for upvote, downvote, posting and commenting:
```bash
python reddit_bot.py
```


Execute the script for all above functionality with DM function:
```bash
python red_bot_withDM.py
```

### Direct Message Feature
- Enter a list of usernames when prompted (comma-separated).
- Provide the subject and body of the message.

Change these accordingly:
```
usernames = ["user1"]
message_subject = ["Subject1"]
message_body = ["Body1"]
```

---

## Example Output

```
Authenticated as: Long_Humor167
Posted to r/test: Hello Reddit!
Commented successfully!
Upvoted successfully!
Enter Reddit usernames to DM (comma-separated): user1, user2
Enter the subject of the message: Greetings
Enter the body of the message: Hello from my Reddit bot!
Message sent to u/user1
Error sending message to u/user2: User does not exist
```

---

## Notes

1. **Rate Limiting**:
   - Reddit enforces rate limits for posting, commenting, and sending DMs. Add delays to avoid being temporarily blocked.
2. **Testing**:
   - Use bot-friendly subreddits like `r/test` for experimentation.
3. **Error Handling**:
   - Errors (e.g., invalid usernames or insufficient permissions) are logged for each action.

---

## Future Enhancements
- Add support for fetching data from subreddits.
- Implement scheduled posting.
- Integrate logging for better debugging.

---

## License
This project is open source and available under the [MIT License](LICENSE).

