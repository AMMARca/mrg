import os


class Config(object):
    API_HASH = os.environ.get("d3f57b56ad8463fc96cc969da6586381")
    BOT_TOKEN = os.environ.get("7156843846:AAFd-xHDZTrvWRD1gxd4K2DwKLXDQ0q2DSo")
    TELEGRAM_API = os.environ.get("17075222")
    OWNER = os.environ.get("7103573952")
    OWNER_USERNAME = os.environ.get("teststtt27")
    PASSWORD = os.environ.get("1502194331aA$")
    DATABASE_URL = os.environ.get("mongodb+srv://hi:hi@cluster0.rbbwg9i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002135850719")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
