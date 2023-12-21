from openpyxl import load_workbook, drawing
from random import randint
from config import jobs_path, images_path

"""Load a workbook, change quantities, save workbook"""


def manipulate_sheet(file):
    # try loading file
    print(file)
    try:
        workbook = load_workbook(filename=file)
    except Exception as e:
        print(e)
    # load sheet from file
    sheet = workbook.active

    # change the invoice number
    sheet["F9"] = randint(123456, 789123)

    # change quantities to random numbers between one and ten
    cellnumbers = [i for i in range(16, 27)]
    for i in cellnumbers:
        sheet["E" + str(i)] = randint(1, 10)

    file_name_parts = str(file).split("\\")
    no_path_file_name = file_name_parts[-1]

    # Add image to file
    image_name = no_path_file_name.split(".")

    try:
        image = f"{images_path}\\{image_name[0]}.png"

        img = drawing.image.Image(image)
        img.anchor = "E4"
        sheet.add_image(img)

    except FileNotFoundError:
        print("File not found")

    # save workbook
    save_path = f"{jobs_path}\\{no_path_file_name}"
    workbook.save(filename=save_path)

    return True
