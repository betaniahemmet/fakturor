from openpyxl import load_workbook
from random import randint
from datetime import datetime

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

    # save workbook
    workbook.save(filename=file)
    return
