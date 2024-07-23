import time

def double_number(number: int):
    return number * 2

def read_last_number_from_file():
    with open("resources/file.txt", "r") as file:
        last_nmumber = int(file.readlines()[-1])
        print(last_nmumber)
        return last_nmumber
    
last_number = read_last_number_from_file()
print(last_number)
doubled_number = double_number(last_number)
print(doubled_number)
time.sleep(1)
