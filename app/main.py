import uvicorn 
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import staticfiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

peers_db = [
    {"name": "Office-Laptop", "status": "Connected", "ip": "10.0.0.2", "usage": "1.2 GB"},
    {"name": "Home-PC", "status": "Offline", "ip": "10.0.0.3", "usage": "450 MB"},
    {"name": "Balajih4kr", "status": "Connected", "ip": "10.0.0.4", "usage": "451 MB"}
]

@app.get('/', response_class = HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "title": "dashboard", "peers": peers_db}
    )



if __name__ == "__main__":
    app.run("main:app", host="127.0.0.1", port=8000, reload=True)
