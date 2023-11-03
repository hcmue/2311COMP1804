from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

@app.get("/")
def Hello():
    return "Hello"


@app.get("/comp1804")
def pypage():
    html = '''<html>
    <head><title>COMP1804</title></head>
    <body>
        <h2>COMP1804 - Lập trình Python
    </body>
</html>
'''
    return HTMLResponse(content=html)

# from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="Buoi07_FastAPI\\templates")
working_directory = os.getcwd()

@app.get("/tradiem/{ma_sv}", response_class=HTMLResponse)
def tra_diem_sinh_vien(request: Request, ma_sv: str):
    data_diem = []
    with open(os.path.join(working_directory, "Buoi07_FastAPI", "students.json"), encoding="utf-8") as mf:
        data_diem = json.load(mf)
    return templates.TemplateResponse(
        "student_template.html", 
        {
            "request": request,
            "ho_ten_sinh_vien": ma_sv,
            "ketqua": data_diem
        }
    )