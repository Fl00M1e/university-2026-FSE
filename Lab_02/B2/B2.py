from pathlib import Path

folder = Path(__file__).resolve().parent

file_name_data = input("Введите название исходного файла :  ")
file_name_report_correct = input("Введите название эталонного файла для сверки : ")
file_name_report = input("Введите название файла который будет создан : ")
input_file = folder / file_name_data
output_file = folder / file_name_report
correct_file = folder / file_name_report_correct

results = []

with open(input_file, "r", encoding="utf-8") as file:
    # Пропуск двух строк заголовка перед данными.
    next(file)
    next(file)

    for line in file:
        data = line.split()
        if len(data) != 3:
            continue

        time, temperature, wind_speed = data
        temperature = int(temperature)
        wind_speed = int(wind_speed)

        # Формула: WC = 35.74 + 0.6215*T + (0.4275*T - 35.75)*V**0.16.
        wc_temperature = (
            35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * wind_speed**0.16
        )
        wc_effect = wc_temperature - temperature
        results.append((time, wc_temperature, wc_effect))

# Среднее = сумма всех значений WC / количество наблюдений.
average = sum(wc_temperature for _, wc_temperature, _ in results) / len(results)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(" Time        WC temp       WC Effect\n")
    file.write("------------------------------------\n")

    for time, wc_temperature, wc_effect in results:
        file.write(f" {time} {wc_temperature:10.1f} {wc_effect:15.1f}\n")

    file.write("------------------------------------\n\n")
    file.write(
        f"The average adjusted temperature based on {len(results)} "
        f"observations, was {average:.1f}\n"
    )

print("Результат сохранён в файл", output_file)
result = output_file.read_text(encoding="utf-8").splitlines()[1:]
correct = correct_file.read_text(encoding="utf-8").splitlines()[1:]
if result == correct:
    print("Расчёты проведены верно")
else:
    print("Расчёты проведены неверно")
