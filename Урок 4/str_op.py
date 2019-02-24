s="У лукоморья 123 дуб зеленый 456"
if s.find('я')==-1:
    print ('1)',"Символ не обнаружен") 
else:
    print ('1)',s.find('я'))

print('2) Буква \'у\' встречается' ,s.count('у'),' раза')

if s.isalpha():
    print ('3) В строке не только буквы')
else:
    print('3)', s.upper())

if len(s)>4:
    print ('4)', s.lower())

print('5)',s.replace ('У','О'))
