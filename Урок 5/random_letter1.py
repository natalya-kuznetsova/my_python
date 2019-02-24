s=['самовар','весна','лето']
import random
word=random.choice(s)
letter=random.choice(word)
print(word.replace(letter,'?'))
answer=str(input('Введите букву: '))
if answer==letter:
    print(word)
else:
    print('Неверно!\nСлово: ',word)

