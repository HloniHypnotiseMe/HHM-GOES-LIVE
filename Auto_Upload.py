HHM-GOES-LIVE: FULLY AUTOMATED YOUTUBE UPLOADER Engine: Python | Platform: GitHub Actions | Hosting: GitHub Repo (Private or Public) Tools: YouTube Data API v3, OAuth 2.0, FFmpeg (optional), ElevenLabs, Synthesia integration coming via webhook 

import os import google_auth_oauthlib.flow import googleapiclient.discovery import googleapiclient.errors from google.oauth2.credentials import Credentials

ENVIRONMENT VARIABLES 

YOUTUBE_CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET") YOUTUBE_CLIENT_ID = os.environ.get("YOUTUBE_CLIENT_ID") YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY") VIDEO_FILE = "episode001.mp4" TITLE = "HYPNOTISE ME FM: Episode 001 — 'Wake Up Drop'" DESCRIPTION = "HYPNOTISE ME FM is 100% AI-powered soul radio. This episode is a morning wake-up drop." TAGS = ["Hloni Hypnotise Me", "Spiritual Radio", "AI Radio", "Awakening"] CATEGORY_ID = "22" # People & Blogs

SCOPES 

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

AUTH + SERVICE 

creds = None if os.path.exists("token.json"): creds = Credentials.from_authorized_user_file("token.json", scopes)

if not creds or not creds.valid: if creds and creds.expired and creds.refresh_token: creds.refresh(Request()) else: flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file( "client_secret.json", scopes ) creds = flow.run_local_server(port=0) with open("token.json", "w") as token: token.write(creds.to_json())

youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

UPLOAD VIDEO 

def upload_video(): request_body = { "snippet": { "categoryId": CATEGORY_ID, "title": TITLE, "description": DESCRIPTION, "tags": TAGS }, "status": { "privacyStatus": "public" } }

mediaFile = googleapiclient.http.MediaFileUpload(VIDEO_FILE, resumable=True) request = youtube.videos().insert( part="snippet,status", body=request_body, media_body=mediaFile ) response = request.execute() print(f"✅ Video uploaded: https://youtu.be/{response['id']}") 

if name == 'main': upload_video()

