
import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

current_datetime1 = datetime.datetime.now().date()
print(current_datetime1)
current_datetime2 = datetime.datetime.now().time()
print(current_datetime2)

time_object1 = datetime.time(12, 30, 45, 123456)
print(time_object1)
time_object2 = datetime.date(2025, 5, 23)
print(time_object2)


duration = datetime.timedelta(days=5, hours=3)
print(duration)

new_date = current_datetime + duration
print(new_date)

birthday = datetime.timedelta(days=5748, hours=6)
print(birthday)

new_date2 = current_datetime - birthday
print(new_date2)

