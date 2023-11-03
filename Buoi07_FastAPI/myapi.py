from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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