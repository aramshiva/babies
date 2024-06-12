> [!NOTE]  
> This does **not** include any social security numbers. The only data stored is the name, frequency, sex, year born
> This **is** public data given by the Social Security Adminstration

# Babies
## A parser for every name listed on a social security card between 1880-2023.
Your first question is probably why? to that I ask why not?

This data is pulled from the [US Social Security Administration's Baby Names from Social Security Card Applications - National Dataset](https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-data).
This script will insert the data into a MySQL database with the following schema:
```
name VARCHAR(255),
sex CHAR(1),
amount INT,
year INT
```

### Some things to keep in note:
- As of 2024 there are around 2,117,219 rows in the database.
- The data is stored in a folder called "names" in the same directory as this script.
- Names with 5 or less occurrences with the sex and year are defaulted to 5 by the SSA to protect privacy
- The sex is a single character, either "M" or "F" for Male or Female.
- The year is the year the person was born, NOT registered.

### Planned Features (when i get bored again):
- Add a new column for the state the name was registered/possibly create a new database to store the [state data](https://www.ssa.gov/oact/babynames/limits.html).
- Create a web interface to search for names and display the data.
- Graphs! Who doesn't love graphs?
- An exported db file for those who don't want to set up a MySQL server :D
