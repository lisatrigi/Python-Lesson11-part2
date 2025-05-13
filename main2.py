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

duration = datetime.timedelta(days=100, hours=100)
print(duration)

new_date1 = current_datetime - duration
print(new_date1)
new_date2 = current_datetime + duration
print(new_date2)

file_path = "C:/Users/Student/Desktop/lesson11/text.txt"
with open(file_path, "w") as file:
    file.write(new_date1)

file_path = "C:/Users/Student/Desktop/lesson11/text.txt"
with open(file_path, "w") as file:
    file.write(new_date2)