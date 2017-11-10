#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import openpyxl
from sys import argv, maxsize
from collections import Counter
from openpyxl.utils.exceptions import IllegalCharacterError

ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')

input_file = 'Drones - 3034 Companies.csv'
output_file = 'RegenWiz.xlsx'
template_file = 'template.xlsx'

# input_file = argv[1]
# output_file = argv[2]
# template_file = argv[3]


# for OverflowError
decrement = True
while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxsize)
    except OverflowError:
        maxsize = int(maxsize/10)
        decrement = True

book = openpyxl.load_workbook(template_file)
raw_sheet = book.get_sheet_by_name("Raw Data")
magic_sheet = book.get_sheet_by_name("Magic")

raw_title = ['Node ID', 'Keywords']
magic_title = ['Keyword', 'Count - Keyword','Blacklist','Boost']

with open(input_file,encoding='utf-8') as csvFile:
    raw_ceil = 2
    magic_ceil = 5
    counts = Counter([])
    reader = csv.DictReader(csvFile)

    for row in reader:
        words = list(map(str.strip,row[raw_title[1]].split(';')))
        nodeid = row[raw_title[0]]
        counts.update(words)
        for r, word in enumerate(words):
            raw_sheet.cell(row=raw_ceil,column=1).value = nodeid
            try:
                raw_sheet.cell(row=raw_ceil,column=2).value = word
            except IllegalCharacterError:
                word = re.sub(ILLEGAL_CHARACTERS_RE,'',word)
                raw_sheet.cell(row=raw_ceil,column=2).value = word
            raw_ceil+=1

    for key,freq in counts.items():
        try:
            magic_sheet.cell(row=magic_ceil,column=1).value = key
        except IllegalCharacterError:
            key = ILLEGAL_CHARACTERS_RE.sub('',key)
            raw_sheet.cell(row=raw_ceil,column=1).value = key
        magic_sheet.cell(row=magic_ceil,column=2).value = freq
        magic_ceil+=1
    magic_sheet.cell(row=magic_ceil,column=1).value = "Total Result"
    magic_sheet.cell(row=magic_ceil,column=2).value = sum(counts.values())
book.save(output_file)
