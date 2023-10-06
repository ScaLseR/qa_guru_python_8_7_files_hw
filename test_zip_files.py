"""Домашняя работа: Создать новые тесты, которые заархивируют имеющиеся в resources различные типы файлов
(xls, xlsx, pdf, txt) в один архив, отправят его в tmp и проверят тестом в архиве каждый из файлов,
что он является тем самым, который был заархивирован, не распаковывая архив."""
import os
from utils import RESOURCES_PATH
from zipfile import ZipFile


def test_zip_files_from_resources_names(tmp_dir):
    """Проверяем наличие в созданном архиве всех файлов по списку имен"""
    # получаем список имен файлов в resources
    file_in_dir = os.listdir(RESOURCES_PATH)
    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        assert file_in_dir == zf.namelist()


def test_zip_file_text(tmp_dir):
    """Проверяем соответствие размеров исходного и файла в архиве,
    + проверка файла по содержимому"""
    txt_file_size = os.path.getsize(os.path.join(RESOURCES_PATH, 'Hello.txt'))
    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        # проверяем на соответсвие размеру файла
        assert txt_file_size == zf.getinfo('Hello.txt').file_size
        # проверяем по содержимому
        assert 'Hello world' in zf.read('Hello.txt').decode()
