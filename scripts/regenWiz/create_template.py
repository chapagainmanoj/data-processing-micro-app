#!/usr/bin/env python

from openpyxl.utils import get_column_letter
import openpyxl

# sample_file = argv[1]
# template_file = argv[2]

sample_file = 'Regeneration Wizard-Sample Output.xlsx'
template_file = 'template.xlsx'

raw_ceil = 2
magic_ceil = 4

book = openpyxl.load_workbook(sample_file)

raw_sheet = book.get_sheet_by_name("Raw Data")
magic_sheet = book.get_sheet_by_name("Magic")

for row in raw_sheet['A2:B60821']:
    for cell in row:
        cell.value = None

for row in magic_sheet['A5:D6461']:
    for cell in row:
        cell.value = None
book.save(template_file)
