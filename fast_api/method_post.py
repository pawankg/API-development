from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students_dict = {
    1: {
        "name": "Tom",
        "age": 12,
        "class_year": 8
    },
    2: {
        "name": "John",
        "age": 16,
        "class_year": 12
    }
}

class Student(BaseModel):
    name: str
    age: int
    class_year: int

@app.get("/student-details/{student_id}")
# def fetch_student_details(student_id: int):        # Simple way of function definition
# Path(None, description="Student ID for fetching details", gt=0, lt=4)) means default value is None, then description
# of the field, then constraints on the value of student_id that can be entered by the user (greater than 0 and less
# than 4)
# Example of Path parameters
def fetch_student_details(student_id: int = Path(None, description="Student ID for fetching details", gt=0, lt=4)):
    if student_id in students_dict.keys():
        data = students_dict[student_id]
    else:
        data = "Details not found!"
    return data #students_dict[student_id]


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students_dict.keys():
        return {"Error": "Student already exists!"}

    students_dict[student_id] = student
    return students_dict[student_id]
