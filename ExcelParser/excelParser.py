#!python
# Uses Python 3
# needs to install openpyxl

from openpyxl import load_workbook

wb = load_workbook("./parse.xlsx")

print(wb.sheetnames)

for sheet in wb:
  if sheet.title == "GlossaryNotes":
    continue
  # Take sheet name, trim the 'n - ' (Where n is a number) and set it as character name
  