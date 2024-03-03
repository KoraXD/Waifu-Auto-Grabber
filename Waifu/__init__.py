# © Waifu Auto Grabber

"""
🔥 Developers:
     ⚡ Kora | @KoraXD
     ⚡ Dark | @IkariS0_0
     ⚡ Otazuki | @Otazuki
"""

import os
import sys
from pyrogram import Client
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

# Vars Stuffs
SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
MONGO_URL = os.environ.get("MONGO_URL")
HANDLER = ["~",".","!","/","$","#"]

# Client Stuffs
Sophia = Client("Waifu-Auto-Grabber", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Waifu/Plugins"))

# Mongo Stuffs
MONGO_DB = MongoClient(MONGO_URL)
DB = MONGO_DB.WAIFUAUTOGRABBER
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["WAIFUAUTOGRABBER"]
