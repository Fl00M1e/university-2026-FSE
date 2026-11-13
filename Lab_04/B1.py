from math import ceil

file = open('input_data/Precip.txt', 'r', encoding='utf-8')

title = file.readline().strip()

place = file.readline().strip()
date = file.readline().strip()

print(place)
print(date)

parts = date.split(',')

month = parts[0]
year = int (parts[1])

print(month)
print(year)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    days_in_month[1] = 29
month_number = months.index(month)
days = days_in_month[month_number]

print(days)

rain = [None] * (days + 1)

errors = [] 
amounts = []


line_number = 3 
for line in file : 
    line_number += 1
    parts = line.split()
    day = int(parts[0])
    amount = float(parts[1])

    print(line_number, day, amount)

    if day < 1 or day > days:
        errors.append(['Invalid', day, line_number])

    elif rain[day] is not None:
        errors.append(['Repeated', day, line_number])

    else: 
        rain[day] = amount 
        amounts.append(amount)

file.close()

report = open('Report.txt', 'w', encoding='utf-8')
report.write('Programmer: Zanevski Dariush\n')
report.write(title + '\n\n')

report.write(
    f"Precipitation report for {place} during {month}, {year}\n\n"
)
report.write('Error         Day        Line\n')
for error in errors: 
    report.write(f'{error[0]:<10}{error[1]:>7}{error[2]:>11}\n')

report.write('\nDay     Amount     Graph\n')
for day in range(1, days + 1):
    if rain[day] is None: 
        report.write(f'{day:3}{'NA':>6}\n')

    else: 
        stars = '*' * ceil(rain[day] / 0.25)
        report.write(f'{day:3} {rain[day]:6.2f} {stars}\n')

report.write('\nMinimum     Maximum     Average\n')

if len(amounts) == 0: 
    report.write(f'{"NA":>7}{"NA":>12}{"NA":>12}\n')
else:
    minimum = min(amounts)
    maximum = max(amounts)
    average = sum(amounts) / days 

    report.write(f'{minimum:7.2f}{maximum:12.2f}{average:12.2f}\n')

report.close()




































































































































































