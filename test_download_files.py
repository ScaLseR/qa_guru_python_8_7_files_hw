"""Домашняя работа: Создать новые тесты, которые заархивируют имеющиеся в resources различные типы файлов
(xls, xlsx, pdf, txt) в один архив, отправят его в tmp и проверят тестом в архиве каждый из файлов,
что он является тем самым, который был заархивирован, не распаковывая архив."""
import os
from utils import RESOURCES_PATH
from zipfile import ZipFile


def test_zip_files_from_resources(tmp_dir):
    # получаем список имен файлов для дальнейшего использования в тестах
    file_in_dir = os.listdir(RESOURCES_PATH)
    # создаем zip архив в директории tmp со всеми файлами находящимися в resources
    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='w') as zf:
        for file in file_in_dir:
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file, arcname=add_file.split("\\")[-1])

    # проверяем наличие всех файлов в созданном архиве по списку имен
    with ZipFile(os.path.join(tmp_dir, 'test.zip'), mode='r') as zf:
        assert file_in_dir == zf.namelist()

