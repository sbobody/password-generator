import random 
special_symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
number_symbol = int(input('Длина вашего пароля ?'))
generation = ''
for i in range(number_symbol):
    char = special_symbol[random.randint(0, len(special_symbol) - 1)]
    generation += char
print (generation)