movie=input("Выберите фильм: ")
day=input("Выберите день (сегодня, завтра): ")
time=int(input("Выберите время: "))
numb=int(input("Выберите количество билетов: "))
def sale(number,day):
    pass
    if day=="завтра" and number>=20:
           return sum(0.2,0.05)
    elif day=="завтра":
           return 0.05
    elif number>=20:
           return 0.2
    else:
           return 0
def price(movie,time):
    pass
    if movie=="Пятница":
        if time==12:
            return 250
        elif time==16:
            return 350
        elif time==20:
            return 450
        else:
            return 0
    elif movie=="Чемпионы":
        if time==10:
            return 250
        elif time==13:
            return 350
        elif time==16:
            return 350
        else:
            return 0
    elif movie=="Пернатая банда":
        if time==10:
            return 350
        elif time==14:
            return 450
        elif time==18:
            return 450
        else:
            return 0
    else:
        return 0

print("Итого: ", price(movie,time)*(1-sale(numb,day))*numb, " руб.")
           
