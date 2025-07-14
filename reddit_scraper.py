import praw
from dotenv import load_dotenv
import os

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
    )

def scrape_user_content(username, max_items=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for post in user.submissions.new(limit=max_items):
            posts.append({
                'title': post.title,
                'body': post.selftext,
                'score': post.score,
                'subreddit': str(post.subreddit),
                'url': post.url,
                'permalink': f"https://reddit.com{post.permalink}"
            })
    except Exception as e:
        print(f"[Error fetching posts]: {e}")

    try:
        for comment in user.comments.new(limit=max_items):
            comments.append({
                'body': comment.body,
                'score': comment.score,
                'subreddit': str(comment.subreddit),
                'permalink': f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"[Error fetching comments]: {e}")

    return {'posts': posts, 'comments': comments}
