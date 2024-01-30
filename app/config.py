from pathlib import Path

fakturor_path = Path(__file__).parents[1]  # The path to fakturor folder

invoices_path = fakturor_path / "invoices"  # The path to invoices templates

jobs_path = fakturor_path / "jobb"  # The path to where the invoices go when ready

images_path = fakturor_path / "images"  # The path to the images for the invoices

mag_path = fakturor_path / "orders"  # The path to orders

test_temp_folder_path = (
    fakturor_path / "test_temp_folder"
)  # A folder to test test-functions on

secret = "askimsviken"
