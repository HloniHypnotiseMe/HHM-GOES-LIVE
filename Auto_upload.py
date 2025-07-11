import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Load secrets from environment
API_KEY = os.getenv("YOUTUBE_API_KEY")
VIDEO_FILE = "demo_video.mp4"  # Change to actual video name
TITLE = "Hypnotise Me FM: Episode 1"
DESCRIPTION = "The first drop of the revolution. #ChangeYourMindChangeYourLife"
TAGS = ["Hloni", "Hypnotise Me", "Spiritual", "Awakening"]
CATEGORY_ID = "22"  # People & Blogs
PRIVACY = "public"  # or "unlisted" or "private"

# Auth and YouTube API init
youtube = build("youtube", "v3", developerKey=API_KEY)

# Upload media
media = MediaFileUpload(VIDEO_FILE)

# Build request
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": TITLE,
            "description": DESCRIPTION,
            "tags": TAGS,
            "categoryId": CATEGORY_ID,
        },
        "status": {
            "privacyStatus": PRIVACY
        },
    },
    media_body=media
)

response = request.execute()
print("✅ Uploaded:", response["id"])
print("🔗 Link: https://youtu.be/" + response["id"])
