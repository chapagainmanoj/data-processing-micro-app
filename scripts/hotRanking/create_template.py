#!/usr/bin/env python

from openpyxl.utils import get_column_letter
import openpyxl

# sample_file = argv[1]
# template_file = argv[2]

# copy formula from a row to entire sheet
# def copy_formulae(ws, r_index,t_index):
#     r_index, t_index = str(r_index), str(t_index)
#     row = [x.value.replace(r_index,t_index)|None for x in (list(op_company_ranking.rows)[5])]
#     print (row)
#     return row


sample_file = 'Ranking companies and clusters using Quid metrics v4 (Sample Output).xlsx'
template_file = 'template.xlsx'

raw_ceil = 2
magic_ceil = 4

book = openpyxl.load_workbook(sample_file)


ip_companies_list = book.get_sheet_by_name("Input - companies list")
ip_target_report = book.get_sheet_by_name("Input - target event report")
op_company_ranking = book.get_sheet_by_name("Output  - Company ranking")
op_cluster_ranking = book.get_sheet_by_name("Output - Cluster ranking")

for row in ip_companies_list['A2:AL584']:
    for cell in row:
        cell.value = None

for row in ip_target_report['A3:K326']:
    for cell in row:
        cell.value = None

for row in op_company_ranking['A3:R585']:
    for cell in row:
        cell.value = None

for row in op_cluster_ranking['A3:M15']:
    for cell in row:
        cell.value = None

book.save(template_file)
