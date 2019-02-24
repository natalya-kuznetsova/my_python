s=str(input('Напишите что-нибудь: '))
n=int(input('Введите число: '))
def func(s,n):
    if len(s)>n:
        return s.upper()
    else:
        return s
print(func(s,n))
