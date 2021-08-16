from src import __version__
import pytest

from src.main import app
from src.db import mongo
from src.config import settings
from bson import ObjectId


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.asyncio
async def test_mongo_connection_with_env_vars():
    await mongo.start_mongo(encrypted=False)
    record = await app.mongodb[settings.DB_NAME].find_one({'connection': True})
    assert isinstance(record.get('_id'), ObjectId)


def test_reset_script_for_field_level_enc_and_unenc_documents_in_mongo():
    # TODO `manage.py` : reset script for field level encrypted and unencrypted documents in a Mongo collection
    assert False


def test_integreate_csfle_with_motor_fastapi():
    # TODO integrate CSFLE with motor
    assert False


def test_dockerise_inc_makefile():
    # TODO Dockerise with makefile
    assert False


def test_add_beanie_with_simple_fastapi_route_to_list_all_documents_without_encryption():
    # TODO Add Beanie with simple FastAPI route to list all documents without encryption
    assert False
