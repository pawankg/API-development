from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def first_func():
    return "Welcome to the FastAPI world!"
