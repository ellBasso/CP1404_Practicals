from prac_06.guitar import Guitar

year = 1922
cost = 16035.40
guitar = Guitar("Gibson L-5 CES", year, cost)
print(f"Age = {guitar.get_age()} - expected 99")
print(f"Vintage = {guitar.is_vintage()} - expected vintage = True")
print(guitar)
