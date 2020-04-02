import re

name_part = r"[a-zA-Z\.]+"
name = f"{name_part}(?: {name_part})?"
name_pattern = re.compile(f"({name_part})(?: ({name_part}))")

etal = r"et al\."

names = f"{name}(?: and {name})*(?: {etal})?"
names_pattern = re.compile(f"({name}(?: and {name})*)(?: {etal})?")

year = r"\d{4}(?:[a-z](?:, [a-z])*)?"
year_pattern = re.compile(year)

years = f"{year}(?:, {year})*(?: and references therein)?"
years_pattern = re.compile(f"({year}(?:, {year})*)(?: and references therein)?")

names_years = f"{names}, {years}"
names_years_pattern = re.compile(f"({names}), ({years})")

many_names_years = f"{names_years}(?:; {names_years})*"
many_names_years_pattern = re.compile(many_names_years)

# years_pattern = re.compile(years)
# name_pattern = re.compile(name)

if __name__ == "__main__":
    print(many_names_years)
