# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "18694811"))
API_HASH = getenv("API_HASH", "2257d0135b9034aa25b307ba3c47f004")
BOT_TOKEN = getenv("BOT_TOKEN", "7137840331:AAG_UXhuVdd-Ewh4Jub5c7B9V0A-kVmLvfs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1248187876").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://theghost:TheGHOST1123@youtubedownloader.kn2hbxl.mongodb.net/?retryWrites=true&w=majority&appName=YoutubeDownloader")
LOG_GROUP = getenv("LOG_GROUP", "-1002074468541")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002193002882"))
