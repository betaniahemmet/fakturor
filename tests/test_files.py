import pytest
from ..app.config import invoices_path, jobs_path, mag_path, test_temp_folder_path
from ..app.file_functions import (
    choose_files,
    take_inventory,
    copy,
    clean_out_folder,
    create_invoices,
    magnus_order,
)
from pathlib import Path
import os


def create_test_folder():
    """Create test folder"""
    if not test_temp_folder_path.is_dir():
        os.mkdir(test_temp_folder_path)
    else:
        pass


def create_test_files():
    """Create files in test folder"""
    for i in range(5):
        file = open(test_temp_folder_path / f"test_file{i}.txt", "w")
        file.write(f"test {i}")
        file.close()


def delete_test_folder():
    """Delete test folder"""
    clean_out_folder(test_temp_folder_path)
    os.rmdir(test_temp_folder_path)


def test_paths():
    """Test paths from config"""
    assert invoices_path.is_dir()
    assert jobs_path.is_dir()
    assert mag_path.is_dir()


def test_choose_files():
    """Test choose files"""
    files = take_inventory(invoices_path)
    files_chosen = choose_files(files, 3)
    assert type(files_chosen) == list
    assert len(files_chosen) == 3


def test_clean_out_folder():
    """Test clean out folder"""
    create_test_folder()
    create_test_files()

    file_check = take_inventory(test_temp_folder_path)
    assert len(file_check) == 5

    clean_out_folder(test_temp_folder_path)

    second_file_check = take_inventory(test_temp_folder_path)
    assert len(second_file_check) == 0

    delete_test_folder()


def test_copy():
    """Test copy"""
    create_test_folder()
    test_file = take_inventory(invoices_path)[0]
    copy(test_file, test_temp_folder_path)
    file_check = take_inventory(test_temp_folder_path)

    assert len(file_check) == 1

    delete_test_folder()


def test_create_invoices():
    """Test create invoices"""
    create_invoices(2)
    file_check = take_inventory(jobs_path)
    assert len(file_check) == 2
    clean_out_folder(jobs_path)


def test_magnus_order():
    """Test magnus order"""
    magnus_order()
    file_check = take_inventory(jobs_path)
    assert len(file_check) == 1
    clean_out_folder(jobs_path)
