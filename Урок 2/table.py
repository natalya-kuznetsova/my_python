value = input("Введите номер химического элемента: ")
if value:
    number = int(value)
    if number == 3:
        print("Li")
    elif number == 25:
        print("Mn")
    elif number == 80:
        print("Hg")
    elif number == 17:
        print("Cl")
    else:
        print("Элемент не найден")
else:
    print("Введите номер химического элемента!")
