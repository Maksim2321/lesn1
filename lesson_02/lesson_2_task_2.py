def is_year_leap(year):
    return year % 4 == 0

#Пример: True
test_year = 2024
result = is_year_leap(test_year)
print(f"год {test_year}: {result}")
#Привер: False
test_year_2 = 2023
result_2 = is_year_leap(test_year_2)
print(f"год {test_year_2}: {result_2}")
