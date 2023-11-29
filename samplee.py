day = int(input("No. of days: "))
if day != 0:
    if day < 365:
        year = 0
        week = day // 7
        days = day % 7
    else:
        year = day // 365
        week = (day % 365) // 7
        days = (day % 365) % 7

else:
    year = 0
    week = 0
    days = 0

print("NO. year: ", year)
print("No. Weeks: ", week)
print("No.days", days)