import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MusicJoker7x")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "J0KER_7x")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "776886547").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ت م ا غ س ش ك").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/786a1cee38308f08a74e1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("https://github.com/JOKER-7X/BAKAR_MIC")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
