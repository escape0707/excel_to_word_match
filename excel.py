from itertools import filterfalse

from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.styles import colors
from copy import copy

from excel_match_pattern import (
    many_names_years_pattern,
    names_years_pattern,
    names_pattern,
    years_pattern,
    name_pattern,
    year_pattern,
)


def parse_authors_and_years(authors_years_group):
    for authors_years in authors_years_group:
        authors_and_years = map(str.strip, authors_years.split(","))
        authors = next(authors_and_years).split()
        years = tuple(authors_and_years)
        yield tuple(filterfalse(lambda s: s in ("and", "et", "al."), authors)), years


def change_cell_font_color_to_red(row, col):
    cell = ws.cell(row_no, col_no)
    problematic_cell_Font = copy(cell.font)
    problematic_cell_Font.color = colors.RED
    cell.font = problematic_cell_Font


wb = load_workbook("table2.xlsx")
ws = wb.active
col_no = 17

for col in ws.iter_cols(
    min_col=col_no, max_col=col_no, min_row=5, max_row=221, values_only=True
):
    val: str
    for i, val in enumerate(col):
        row_no = i + 5
        if val:  # skip None
            match = many_names_years_pattern.fullmatch(val)
            if not match:
                print(row_no)
                change_cell_font_color_to_red(row_no, col_no)
                continue
            # print(names_years_pattern.findall(val))
# wb.save("new_table2.xlsx")
