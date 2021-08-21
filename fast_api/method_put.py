from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

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

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_year: Optional[int] = None


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


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students_dict.keys():
        return {"Error": "Student does not exist"}

    # Below statement will assign everything that we have given in put method body to the student_id even if it is NULL
    # students_dict[student_id] = student

    # Correct way is to assign each value separately after checking that it is not NULL
    if student.name != None:
        students_dict[student_id]["name"] = student.name
    if student.age != None:
        students_dict[student_id]["age"] = student.age
    if student.class_year != None:
        students_dict[student_id]["class_year"] = student.class_year

    return students_dict[student_id]
