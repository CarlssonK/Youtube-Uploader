import datetime
import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# upload_date_time = datetime.datetime(2021, 1, 3, 12, 30, 0).isoformat() + '.000Z'


# Get current directory path
mypath = os.path.dirname(os.path.realpath(__file__))

# Get files in this directory path
files = os.listdir(mypath)

# Get the video file
for f in files:
  if ".mp4" in f:
    video = f


request_body = {
    'snippet': {
        'categoryId': 24,
        'title': "your_title_here",
        'description': "your_description_here",
        'tags': ["tag1", "tag2", "tag3"]
    },
    'status': {
        'privacyStatus': 'private',
        # 'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

# Upload Video
mediaFile = MediaFileUpload(video)

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()


# service.thumbnails().set(
#     videoId=response_upload.get('id'),
#     media_body=MediaFileUpload('thumbnail.jpg')
# ).execute()