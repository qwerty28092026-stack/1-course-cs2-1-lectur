import random
 
secret = random.randint(1, 100)   # компьютер загадывает число
guess = 0
tries = 0
 
while guess != secret:
    guess = int(input("Твоя догадка: "))
    tries = tries + 1
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
 
print("Угадал за", tries, "попыток!")
