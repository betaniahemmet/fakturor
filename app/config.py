from pathlib import Path

# Ensure we are working from the correct root directory (fakturor/)
fakturor_path = Path(__file__).resolve().parent.parent

# Correct folder paths
invoices_path = fakturor_path / "invoices"
jobs_path = fakturor_path / "jobb"
images_path = fakturor_path / "images"
mag_path = fakturor_path / "orders"
test_temp_folder_path = fakturor_path / "test_temp_folder"

secret = "askimsviken"
