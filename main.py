import random

def random_number():
    num = random.randint(1,95)
    print(num)
    return num

def doubled_number(number: int):
    return number *2

def main():
    num = random_number()
    return doubled_number(num)

if __name__ == "__main__":
    doubled_number = main()
    print(doubled_number)
    