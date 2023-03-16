from openpyxl import load_workbook, drawing
from random import randint
from datetime import datetime
from config import images_path
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
    cellnumbers = [i for i in range(15, 27)]
    for i in cellnumbers:
        sheet["E" + str(i)] = randint(1, 10)
    # add image to invoice
    image_name_parts = str(file).split('\\')
    print(image_name_parts[-1])
    image_name = image_name_parts[-1]
    image_name = image_name.split('.')
    image = f'{images_path}\\{image_name[0]}.png'
    print(image)
    img = drawing.image.Image(image)
    img.anchor = 'F5'
    sheet.add_image(img)
    # save workbook
    workbook.save(filename=file)
    return
