# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24605471"))
    API_HASH = getenv("API_HASH", "70d90e6e3a9d6865a6984eedd46aa6cd")
    BOT_TOKEN = getenv("BOT_TOKEN", "6482376899:AAFbHwvqr5KXS5KLvUeZDHE4UZCVcotf_W0")
    FSUB = getenv("FSUB", "temsgstejva")
    CHID = int(getenv("CHID", "-1001969845403"))
    SUDO = list(map(int, getenv("SUDO", "6411754182").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://autoacceptts:autoacceptts@cluster0.ythf0ya.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
