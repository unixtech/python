from fastapi import FastAPI

app = FastAPI()


'''
You will have to fetch the `JSON` data from various sources. 


'''
inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Amul"
    }
}

@app.get('/')
def home():

