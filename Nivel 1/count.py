# Tabela ASCII:
# 97 a 122 - minusculas
# 65 a 90 - maiusculas
# 48 a 57 - numeros

def counter(string):
    numbers = 0 
    uppercase = 0
    lowercase = 0
    special = 0

    for i in word:
        if ord(i) >= 48 and ord(i) <= 57:
            numbers += 1
        elif ord(i) >= 65 and ord(i) <= 90:
            uppercase += 1
        elif ord(i) >= 97 and ord(i) <= 122:
             lowercase += 1
        else:
            special += 1
    print(f'Upper case letters : {uppercase}\n'
                 f'Lower case letters : {lowercase}\n'
                 f'Numbers : {numbers}\n'
                 f'Special Characters : {special}')


word = '*GeEkS4GeEkS*'
counter(word)