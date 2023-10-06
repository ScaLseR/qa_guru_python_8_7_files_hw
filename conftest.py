import os
import shutil
import pytest
from utils import TMP_PATH, RESOURCES_PATH


@pytest.fixture
def tmp_dir():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    yield TMP_PATH

    shutil.rmtree(TMP_PATH, ignore_errors=True)
