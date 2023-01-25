dayToday = 6
monthToday = 12
yearToday = 2022

dayBorn = 10
monthBorn = 9
yearBorn = 2003

try:
    if monthToday > monthBorn or (monthToday == monthBorn and dayToday >= dayBorn):
        print("Полных лет - "+str(yearToday - yearBorn))
    else:
        print("Полных лет - "+str(yearToday - yearBorn - 1))
except Exception:
    print("Что-то не так...")