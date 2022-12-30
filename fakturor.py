from pathlib import Path
import shutil
import random
import os

def copy(files, jobs_path):

    three_numbers = random.sample(range(len(files)), 3)
    print(three_numbers)
    for i in three_numbers:
        shutil.copy(files[i], jobs_path)

def take_inventory(a_path):
    file_paths = a_path.glob('**/*')
    files = [f for f in file_paths if f.is_file()]
    return files

def clean_out_folder(a_path):
    files = take_inventory(a_path)
    if files:
        for i in files:
            os.remove(i)


def main():

    fakturor_path = Path(r'C:/Users/Kusten/Desktop/fakturor')
    jobs_path = Path(r'C:/Users/Kusten/Desktop/jobb')
    
    clean_out_folder(jobs_path)
    files = take_inventory(fakturor_path)
    copy(files, jobs_path)
    

if __name__ == "__main__":
    main()
