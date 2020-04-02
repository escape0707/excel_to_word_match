import re

name_part = r"[a-zA-Z\.]*"
name = f"{name_part}(?: {name_part})?"
etal = r"et al\."
names = f"{name}(?: and {name})*(?: {etal})?"

year = r"\d{4}(?:[a-z](?:, [a-z])*)?"
years = f"{year}(?:, {year})*(?: and references therein)?"
names_years = f"{names}, {years}"

many_names_years = f"{names_years}(?:; {names_years})*"

many_names_years_pattern = re.compile(many_names_years)
names_years_pattern = re.compile(names_years)
names_pattern = re.compile(names)
years_pattern = re.compile(years)
name_pattern = re.compile(name)
year_pattern = re.compile(year)

if __name__ == "__main__":
    print(many_names_years)