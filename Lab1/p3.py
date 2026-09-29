# Determine the age of a person, in number of days.
# Take into account leap years, as well as the date of birth and current date
# (year, month, day).
# Do not use Python's inbuilt date/time functions.
#ok so according to google a leap year counts if year % 400,
#not if year % 100, yes if % 4
def is_leap_year(year):
    if year % 400 == 0:
        return True #years divisible by 400 are leap years
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False #1900, even though it is a multiple of 4, is not a leap year


def days_in_month(year, month):
    #to count the days, soo basically a person can be this many years old
    #+ this many months and days

    if month == 2:
        if is_leap_year(year):
            return 29 #to figure out the situation with february, soo if leap we have more days
        else:
            return 28

    if month == 4 or month == 6 or month == 9 or month == 11: #the months with 30 days
        return 30

    return 31


def days_until_date(year, month, day):
    #basically i call the other functions to see the total number
    #of days from each month and year and just add and add and add

    total_days = 0

    #add all complete years before the given year
    y = 1

    while y < year:
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

        y += 1

    #add all complete months before the given month
    m = 1

    while m < month:
        total_days += days_in_month(year, m)
        m += 1

    #add the days of the current month, basically how many have passed
    total_days += day

    return total_days


def age_in_days(birth_year, birth_month, birth_day,
                current_year, current_month, current_day):

    birth_total = days_until_date(birth_year, birth_month, birth_day)
    current_total = days_until_date(current_year, current_month, current_day)

    return current_total - birth_total


def main():
    print("This program determines a person's age in days.")
    print("Enter the date of birth:")

    birth_year = int(input("Year: "))
    birth_month = int(input("Month: "))
    birth_day = int(input("Day: "))

    print("Enter the current date:")
    current_year = int(input("Year: "))
    current_month = int(input("Month: "))
    current_day = int(input("Day: "))
    result = age_in_days(
        birth_year,
        birth_month,
        birth_day,
        current_year,
        current_month,
        current_day
    )
    print("The person's age in days is:", result)
if __name__ == "__main__":
    main()