#!/usr/bin/env python

import xlsxwriter
import csv
import re
import xlrd
import sys
from sys import argv

# input_file = argv[1]
# output_file = argv[2]
# template_file = argv[3]

input_file = "quid_KOL_news_input.csv"
output_file = "v1_out.xlsx"
template_file = "quid_KOL_news_output_UPDATE.xlsx"

maxInt = sys.maxsize
decrement = True

# for OverflowError
while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

table_names = ['Names','Count of Mentions','Avg. of Flow','Avg. of Inter-Cluster Connectivity',
               'Sum of Social Engagement','Sum of Published Count','Source Rank']
# Populate contents of \'Raw data\' tab (copy/paste from input file)
workbook = xlsxwriter.Workbook(output_file, {'constant_memory':True})
worksheet = workbook.add_worksheet("Raw data")
higest_col = None
people_name = set()
with open(input_file,'rt') as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            if col.isdigit():
                col = int(col)
                worksheet.write_number(r,c,col)
            elif re.match('^-?[0-9]+\.[0-9]+$', col):
                col = float(col)
                worksheet.write_number(r,c,col)
            else:
                worksheet.write(r,c,col)
            higest_col = c
            if(xlsxwriter.utility.xl_col_to_name(c)=='S'):
                result = re.sub(r'\([^)]*\)', '',col)
                people_name |= set([people.strip() for people in result.split(';')])

people_name.discard('People (Any Mention)')
people_name.discard('')

def get_formula(header, row, type=None):
    if  type=='abs':
        if (header == 'Count of Mentions'):
            return '=COUNTIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*")'%(row)
        elif (header == 'Avg. of Flow'):
            return '=IFERROR(AVERAGEIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*",INDEX(\'Raw data\'!$A:$BG,0,MATCH("Betweenness Centrality",\'Raw data\'!$A$1:$BG$1,0))), 0)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return '=IFERROR(AVERAGEIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*",INDEX(\'Raw data\'!$A:$BG,0,MATCH("Inter-Cluster Connectivity",\'Raw data\'!$A$1:$BG$1,0))), 0)'%(row)
        elif (header == 'Sum of Social Engagement'):
            return '=SUMIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*",INDEX(\'Raw data\'!$A:$BG,0,MATCH("Social Engagement",\'Raw data\'!$A$1:$BG$1,0)))' %(row)
        elif (header == 'Sum of Published Count'):
            return '=SUMIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*",INDEX(\'Raw data\'!$A:$BG,0,MATCH("Published Count",\'Raw data\'!$A$1:$BG$1,0)))' %(row)
        elif (header == 'Source Rank'):
            return '=IFERROR(AVERAGEIF(INDEX(\'Raw data\'!$A:$BG,0,MATCH("People (Any Mention)",\'Raw data\'!$A$1:$BG$1,0)),"*"&A%d&"*",INDEX(\'Raw data\'!$A:$BG,0,MATCH("Source Rank",\'Raw data\'!$A$1:$BG$1,0))),0)' %(row)
        else:
            return ''
    elif type =='per':
        if (header == 'Count of Mentions'):
            return 'PERCENTRANK(B:B,B%d)'%(row)
        elif (header == 'Avg. of Flow'):
            return 'PERCENTRANK(C:C,C%d)' %(row)
        elif (header == 'Avg. of Inter-Cluster Connectivity'):
            return 'PERCENTRANK(D:D,D%d)'%(row)
        elif (header == 'Sum of Social Engagement'):
            return 'PERCENTRANK(E:E,E%d)' %(row)
        elif (header == 'Sum of Published Count'):
            return 'PERCENTRANK(F:F,F%d)' %(row)
        elif (header == 'Avg of Flow'):
            return 'PERCENTRANK(C:C,C%d)' %(row)
        elif (header == 'Source Rank'):
            return '=1-PERCENTRANK(G:G,G%d)' %(row)
        else:
            return ''
    else:
        if header == 'Total Score':
            return '=((H%d*Weights!$B$2) + (I%d*Weights!$B$3)+(J%d*Weights!$B$4)+(K%d*Weights!$B$5)+ (L%d*Weights!$B$6)+(M%d*Weights!$B$7))' %(row,row,row,row,row,row)
        elif header == 'Overall Rank':
            return '=RANK(N%d,N:N)' %(row)


wb_read = xlrd.open_workbook(template_file)
sheets = wb_read.sheets()
for sheet in sheets:
    if sheet.name == "Weights":
        ws = workbook.add_worksheet("Weights")
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                ws.write(row,col,sheet.cell(row,col).value)
    elif sheet.name =="Output":
        worksheet2 = workbook.add_worksheet("Output")
        for row in range(2):
            for col in range(sheet.ncols):
                worksheet2.write(row,col,sheet.cell(row,col).value)

                #len_table_names = 13
        for r,val in enumerate(people_name):
            if bool(val and val.strip()) == False:
                continue
            max_col = 0
            for c,header in enumerate(table_names):
                if c == 0:
                    worksheet2.write_string(r+2,c,val)
                else:
                    formula = get_formula(header,r+3,'abs')
                    cell = xlsxwriter.utility.xl_rowcol_to_cell(r+2,c)
                    worksheet2.write_formula(cell, formula)
                    max_col = c
            for c,header in enumerate(table_names):
                if c == 0:
                    pass
                else:
                    max_col += 1
                    formula = get_formula(header,r+3,'per')
                    cell = xlsxwriter.utility.xl_rowcol_to_cell(r+2,max_col)
                    worksheet2.write_formula(cell, formula)

            worksheet2.write_formula(r+2,max_col+1,get_formula('Total Score',r+3))
            worksheet2.write_formula(r+2,max_col+2,get_formula('Overall Rank',r+3))
workbook.close()
