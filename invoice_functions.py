import os
from workbook_functions import manipulate_sheet
from config import invoices_path, jobs_path
import shutil
import random


def choose_files(files, num_invoices):
    """Pick two or three files at random"""
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
            os.remove(i)
    return "Folder is clean"



def create_invoices(num_invoices):
    """Put three random invoices in job folder"""
    clean_out_folder(jobs_path)  # Remove old invoices if present
    files = take_inventory(invoices_path)  # Get the paths to the templates
    rand_files = choose_files(
        files, num_invoices
    )  # Choose two or three files at random
    for file in rand_files:
        manipulate_sheet(file)  # Change the quantities of goods in the invoices
        #copy(file, jobs_path)  # Copy the invoices to where they should be
