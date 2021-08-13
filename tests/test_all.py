from src import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_mongo_connection_with_env_vars():
    # TODO set up mongo connection in FastAPI settings with env vars
    assert False


def test_github_action_to_use_secrets_for_integration_test():
    # TODO .Github action to use secret for integration test
    assert False


def test_unencrypted_connection_through_fastapi():
    # TODO test for unencrypted mongo connection through FastAPI w/settings
    assert False


def test_integreate_csfle_with_motor_fastapi():
    # TODO integrate CSFLE with motor
    assert False


def test_reset_script_for_field_level_enc_and_unenc_documents_in_mongo():
    # TODO `manage.py` : reset script for field level encrypted and unencrypted documents in a Mongo collection
    assert False


def test_dockerise_inc_makefile():
    # TODO Dockerise with makefile
    assert False


def test_add_beanie_with_simple_fastapi_route_to_list_all_documents_without_encryption():
    # Add Beanie with simple FastAPI route to list all documents without encryption
    assert False
