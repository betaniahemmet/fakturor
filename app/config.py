import os
from pathlib import Path

# Check environment variable to determine the base directory
fakturor_path = Path(os.getenv('FAKTUROR_PATH', Path(__file__).parents[1]))  # Default to the parent folder if not set

invoices_path = fakturor_path / "invoices"
jobs_path = fakturor_path / "jobb"
images_path = fakturor_path / "images"
mag_path = fakturor_path / "orders"
test_temp_folder_path = fakturor_path / "test_temp_folder"

secret = "askimsviken"