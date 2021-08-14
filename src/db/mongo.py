from icecream import ic
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientEncryption
from src.config import settings


async def start_mongo(encrypted=True):
    from src.main import app
    ic('starting mongo..')
    try:
        app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
        app.mongodb = app.mongodb_client[settings.DB_NAME]
        await app.mongodb[settings.DB_NAME].update_one({'connection': True}, {"$set": {'connection': True}}, upsert=True)
    except Exception:
        raise Exception(
            'There has been an error. Remember: Environment Variables must be set.')
