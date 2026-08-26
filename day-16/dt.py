from datetime import datetime, date

# day 16 exexercise 1
print("\nday 16 exexercise 1")
today = date.today()
today2 = datetime.today()
print(today.day, today.month, today.year, today2.hour, today2.minute, today2.timestamp())

# day 16 exexercise 2
print("\nday 16 exexercise 2")
print(today2.strftime("%m/%d/%Y, %H:%M:%S"))

# day 16 exexercise 3
print("\nday 16 exexercise 3")
time = date(2019, 12,5)
print(time)
day = "5 December, 2019"
day_to_time = datetime.strptime(day, '%d %B, %Y')
print(day_to_time)

# day 16 exexercise 4
print("\nday 16 exexercise 4")
new_year_date = datetime(2027, 1, 1)
print(new_year_date -  today2)

# day 16 exexercise 5
print("\nday 16 exexercise 5")
start_year_date = datetime(1970, 1, 1)
print(today2 - start_year_date)