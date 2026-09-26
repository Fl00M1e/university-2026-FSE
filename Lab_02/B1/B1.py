from pathlib import Path
file_name_inmap = input("Введите название исходного файла с данными: ")
file_name_outmap = input("Введите название эталонного файла с правильным решением: ")
file_name_outmap_new = input("Введите название файла который будет создан : ")

folder = Path(__file__).resolve().parent

input_file = folder / (file_name_inmap)
output_file = folder / (file_name_outmap_new)
outmap = folder / (file_name_outmap)

file = open(input_file, "r")

first_line = file.readline().split()
count = int(first_line[0])
scale = float(first_line[1])

map_distances = []

for i in range(count):
    distance = float(file.readline())
    map_distances.append(distance)

file.close()

file = open(output_file, "w")

file.write("Zanevski Dariush\n")
file.write("Simple Map Distance Computations\n\n")
file.write("Map Scale Factor:    {:.2f} miles per inch\n\n".format(scale))
file.write("      Map       Mileage\n")
file.write("      Measure   Distance\n")
file.write("============================================================\n")

total_distance = 0

for i in range(count):
    # Формула: расстояние = измерение на карте * масштаб.
    mileage = map_distances[i] * scale

    # Округление до десятых: 
    mileage = int(mileage * 10 + 0.5) / 10
    total_distance += mileage

    file.write("# {:2d} {:6.1f} {:9.1f}\n".format(
        i + 1, map_distances[i], mileage
    ))

file.write("============================================================\n")
file.write("Total Distance: {:6.1f} miles\n".format(total_distance))

file.close()

# Первую строку с именем автора при сравнении не учитываем.
result = output_file.read_text().splitlines()[1:]
correct = outmap.read_text().splitlines()[1:]

if result == correct:
    print("Файлы my_outmap и исходный outmap совпадают")
else:
    print("Файлы my_outmap и исходный outmap не совпадают")

print("Результат сохранён в файл", output_file)
