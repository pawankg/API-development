from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students_dict = {
    1: {
        "name": "Tom",
        "age": 12,
        "class": 8
    },
    2: {
        "name": "John",
        "age": 16,
        "class": 12
    }
}

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


# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_dict.keys():
        return {"Error": "Student does not exist"}

    del students_dict[student_id]
    return {"Message": "Student deleted successfully"}