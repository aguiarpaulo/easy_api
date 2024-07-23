from fastapi import FastAPI
import random

server = FastAPI()

@server.get("/resources")
def random_number():
    num = random.randint(1,95)
    print(num)
    return num