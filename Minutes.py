minute = int(input("Enter minutes: "))
minuteInYear= 60 *24*365
minuteInDay= 60*24
days = int(minute / 1440)
years = int(days / 365)
days -= (365 * years)
print(str(minute) + ' minutes is ' + str(years) + ' years and ' + str(days) + ' days')
