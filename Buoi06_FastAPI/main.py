from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, UploadFile
from typing import Optional
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name = "David Beckham"):
    return {"message":f"Hello {name}."}


# CRUD Student
JSON_FILE = "student.json"

@app.get("/students", tags=["Student"])
def get_all_students():
    return read_json_file()

@app.get("/students/search", tags=["Student"])
def search_students(name: str | None, gpa: float | None):
    data = read_json_file()
    data_filter = list(filter(lambda sv: name in sv["fullName"], data))
    
    return data_filter

def read_json_file():
    try:
        with open(JSON_FILE, encoding="utf-8") as f:
            return json.load(f)
    except:
        return None
    
@app.get("/students/{id}", tags=["Student"])
def get_student_by_id(id):
    data = read_json_file()
    if data is None:
        raise HTTPException(status_code=500, detail=f"File doesn't exist")
    for student in data:
        if student["studentId"] == id:
            return {
                "success": True,
                "data": student
            }
    # return {
    #     "success": True,
    #     "message": "Not found"
    # }
    raise HTTPException(status_code=404, detail=f"Not found student with id={id}")

class Student(BaseModel):
    studentId: str
    fullName: str
    gpa: float
    gender: bool
    
@app.post("/students", tags=["Student"])
def add_new_student(student: Student):
    # Convert obj ==> dict (viết thêm hàm convert vô lớp Student)
    student_dict = {
        "studentId" : student.studentId,
        "fullName": student.fullName,
        "gpa": student.gpa,
        "gender": student.gender
    }
    data = read_json_file()
    if data is None: # File empty
        data = [student_dict]
    else: # Có dữ liệu
        data.append(student_dict)
        
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    return student

@app.put("/students/{id}", tags=["Student"])
def update_student_by_id(id, student):
    pass

@app.delete("/students/{id}", tags=["Student"])
def delete_student_by_id(id):
    pass



import os
import shutil

UPLOAD_FILE_DIRECTORY = os.getcwd()

@app.post("/images/upload")
def upload_single_file(file: UploadFile):
    try:
        with open(os.path.join(UPLOAD_FILE_DIRECTORY, "data", file.filename), "wb") as myfile:
            shutil.copyfileobj(file.file, myfile)
        return {"message": "Upload file successful."}
    
    
    except:
        return {"message": "Upload file fail."}