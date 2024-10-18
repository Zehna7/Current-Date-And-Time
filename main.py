from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent date and time is", now)

print("\nDate components are", today.day, today.month, today.year)