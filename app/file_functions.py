import random
import shutil
from pathlib import Path
from .workbook_functions import manipulate_sheet
from .config import invoices_path, jobs_path, mag_path


def choose_files(files, num_invoices):
    """Pick one, two or three files at random"""
    rand_numbers = random.sample(range(len(files)), num_invoices)
    rand_files = [files[i] for i in rand_numbers]
    return rand_files


def copy(file, a_path):
    """Copy file from one place to another"""
    try:
        shutil.copy(file, a_path)
    except Exception as e:
        print(e)

    return "Files were copied"


def take_inventory(a_path):
    """See what's in a folder"""
    file_paths = a_path.glob("**/*")
    try:
        files = [f for f in file_paths if f.is_file()]
    except Exception as e:
        print(e)

    return files


def clean_out_folder(a_path):
    """Remove files from jobs folder if files are present"""
    files = take_inventory(a_path)
    if files:
        for i in files:
            Path.unlink(i)
    return "Folder is clean"


def create_invoices(num_invoices):
    """Put one, two or three random invoices in job folder"""
    counter()
    clean_out_folder(jobs_path)  # Remove old invoices if present
    files = take_inventory(invoices_path)  # Get the paths to the templates
    rand_files = choose_files(files, num_invoices)  # Choose files at random
    for file in rand_files:
        manipulate_sheet(file)  # Change quantities of goods in the invoices
        # copy(file, jobs_path)  # Copy the invoices to where they should be


def magnus_order():
    """Make order for M&F"""
    counter()
    clean_out_folder(jobs_path)  # Remove old invoices if present
    file = take_inventory(mag_path)
    manipulate_sheet(file[0])


def counter():
    """Log usage of script"""
    try:
        with open("usage.txt", "r") as f:
            current_number = int(f.readline()) # Read number from file
    except FileNotFoundError:
        current_number = 0

    with open("usage.txt", "w") as f:
        f.write(str(current_number + 1))  # Add one to current number and write or create usage file
