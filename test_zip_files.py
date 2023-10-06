"""Домашняя работа: Создать новые тесты, которые заархивируют имеющиеся в resources различные типы файлов
(xls, xlsx, pdf, txt) в один архив, отправят его в tmp и проверят тестом в архиве каждый из файлов,
что он является тем самым, который был заархивирован, не распаковывая архив."""
import os
from utils import RESOURCES_PATH
from zipfile import ZipFile
from xlrd import open_workbook


def test_zip_files_from_resources_names(tmp_dir):
    """Проверяем наличие в созданном архиве всех файлов по списку имен"""
    # получаем список имен файлов в resources
    file_in_dir = os.listdir(RESOURCES_PATH)
    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        assert file_in_dir == zf.namelist()


def test_zip_file_txt(tmp_dir):
    """Проверяем соответствие размеров исходного txt и файла в архиве,
    + проверка файла по содержимому"""
    # получаем размер исходного файла
    txt_file_size = os.path.getsize(os.path.join(RESOURCES_PATH, 'Hello.txt'))
    # получаем содержимое исходного файла
    with open(os.path.join(RESOURCES_PATH, 'Hello.txt'), 'r') as f:
        txt_file_text = f.read()

    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        # проверяем на соответствие размеру файла
        assert txt_file_size == zf.getinfo('Hello.txt').file_size
        # проверяем по содержимому
        assert txt_file_text in zf.read('Hello.txt').decode()


def test_zip_file_xls(tmp_dir):
    """Проверяем соответствие размеров исходного xls и файла в архиве,
    + проверка файла по содержимому"""
    # получаем размер исходного файла
    xls_file_size = os.path.getsize(os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls'))
    # получаем содержимое исходного xls файла
    book = open_workbook(os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls'))
    sheets_count = book.nsheets
    sheets_names = book.sheet_names()
    xls_file_text = book.sheet_by_index(0).cell_value(9, 3)

    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        # проверяем на соответствие размеру файла
        assert xls_file_size == zf.getinfo('file_example_XLS_10.xls').file_size
        # получаем содержимое xls файла в zip архиве
        book_zip = open_workbook(file_contents=zf.read('file_example_XLS_10.xls'))
        # проверяем по количеству листов
        assert sheets_count == book_zip.nsheets
        # проверяем по названию листов
        assert sheets_names == book_zip.sheet_names()
        # проверяем по содержимому
        assert xls_file_text == book_zip.sheet_by_index(0).cell_value(9, 3)


