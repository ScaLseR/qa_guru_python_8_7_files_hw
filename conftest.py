import os
import shutil
import pytest
from utils import TMP_PATH, RESOURCES_PATH
from zipfile import ZipFile


@pytest.fixture(autouse=True, scope='session')
def tmp_dir():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    # создаем zip архив в директории tmp со всеми файлами находящимися в resources
    with ZipFile(os.path.join(TMP_PATH, 'test.zip'), mode='w') as zf:
        for file in os.listdir(RESOURCES_PATH):
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file, arcname=add_file.split("\\")[-1])

    yield

    shutil.rmtree(TMP_PATH, ignore_errors=True)
