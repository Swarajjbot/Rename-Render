# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26558850")

API_HASH = os.environ.get("API_HASH", "410f922c49c8867b5c8e28d624581b02")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7047795447:AAF9iNhWzPU5PRSBhrv3TS0x3UIXKiz9chY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "INDORECINEMAS5") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "test08")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://test08:test08@cluster0.jit72we.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
