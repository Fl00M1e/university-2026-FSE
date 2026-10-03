from pathlib import Path

print ("Введите название файла с входными данными: ")
file_name = input() #вводим название файла с входными данными


folder = Path(__file__).resolve().parent
file_path = folder.parent / "inmap_data" / file_name #достём размер карты из inmap_data/1.ChaseData.txt посредством библиотеки pathlib

with open(file_path, "r") as file: 
    first_line = file.readline()
    commands = file.readlines() 

width, height = map(int, first_line.split()) #задаём размеры поля доставая их из первой строки входных данных

mouse_x = None
mouse_y = None 
cat_x = None 
cat_y = None

mouse_path = 0
cat_path = 0
mouse_caught = False

print("Cat and Mouse")
print()
print("  Cat        Mouse    Distance")
print("------------------------------")

for line in commands:
    parts = line.split()   #разделяем команду и координаты по пробелу
    command = parts[0]     #извлекаем команду

    if command == "P":
        if cat_x is None:
            cat_position = "( ?, ?)"
        else:
            cat_position = f"({cat_x:2},{cat_y:2})"

        if mouse_x is None:
            mouse_position = "( ?, ?)"
        else:
            mouse_position = f"({mouse_x:2},{mouse_y:2})"

        if cat_x is not None and mouse_x is not None:
            distance = abs(cat_x - mouse_x) + abs(cat_y - mouse_y)
            print(f"{cat_position}     {mouse_position}{distance:8}")
        else:
            print(f"{cat_position}     {mouse_position}")

    else:
        dx = int(parts[1])
        dy = int(parts[2])

        if command == "M":    # "ходьба" мыши 
            if mouse_x is None:
                mouse_x = dx
                mouse_y = dy
            else:
                mouse_x = (mouse_x + dx - 1) % width + 1
                mouse_y = (mouse_y + dy - 1) % height + 1
                mouse_path += abs(dx) + abs(dy)

        elif command == "C":    # "ходьба" кота
            if cat_x is None:
                cat_x = dx
                cat_y = dy
            else:
                cat_x = (cat_x + dx - 1) % width + 1
                cat_y = (cat_y + dy - 1) % height + 1
                cat_path += abs(dx) + abs(dy)

        if cat_x is not None and mouse_x is not None:
            if cat_x == mouse_x and cat_y == mouse_y:    #проверка поимки мыши котом
                mouse_caught = True
                break

print("------------------------------")
print()
print()
print("Distance   Mouse    Cat")
print(f"{mouse_path:16}{cat_path:7}")
print()

if mouse_caught:
    print(f"Mouse caught at: ({mouse_x:2},{mouse_y:2})")
else:
    print("Mouse evaded Cat")
