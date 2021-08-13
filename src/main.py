from typing import Optional
from fastapi import FastAPI
from src.config import settings
from src.db.mongo import start_mongo

import uvicorn
app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
async def startup_db_client():
    """Todo. refactor to start_mongo which should try/except for valid token
    and fallback to start_unencrypted if there is an EncryptionError when performing test query.
    """
    await start_mongo()


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run(app, port=8228, host='127.0.0.1')
