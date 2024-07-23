import random
import time

def random_number():
    num = random.randint(1,95)
    print(num)
    with open("resources/file.txt", "a") as file:
        file.write(f"{num}\n")


random_number()