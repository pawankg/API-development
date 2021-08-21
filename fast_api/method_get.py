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


# Example of Query parameters
@app.get("/fetch-details-by-name")
# (name: str = None), name is of string type and None makes entering this input value optional from required.
def fetch_student_details(inp_name: Optional[str] = None):
    for student_id in students_dict:
        if students_dict[student_id]["name"] == inp_name:
            return students_dict[student_id]
    return {"Data": "Not Found"}
