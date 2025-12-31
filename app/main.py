import uvicorn
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import staticfiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import engine, get_db
from db import models


app = FastAPI()

templates = Jinja2Templates(directory="templates")

peers_db = [
    {"name": "Office-Laptop", "status": "Connected", "ip": "10.0.0.2", "usage": "1.2 GB"},
    {"name": "Home-PC", "status": "Offline", "ip": "10.0.0.3", "usage": "450 MB"},
    {"name": "Balajih4kr", "status": "Connected", "ip": "10.0.0.4", "usage": "451 MB"}
]


@app.post("/peers/create")
async def create_peer(
    developer_name: str = Form(...),
    device_name: str = Form(...),
    public_key: str = Form(...),
    db: Session = Depends(get_db)
):
    # 1. (Optional) Simple logic to pick the next IP
    # In a real app, you'd calculate the next available IP in the 10.0.0.x range
    assigned_ip = "10.0.0.15/32" 

    # 2. Create the Database Record
    new_peer = Peer(
        developer_name=developer_name,
        device_name=device_name,
        public_key=public_key.strip(),
        assigned_ip=assigned_ip,
        status="Offline"
    )
    
    db.add(new_peer)
    db.commit()
    db.refresh(new_peer)

    # 3. Redirect back to the dashboard to see the new card
    return RedirectResponse(url="/", status_code=303)



@app.get('/', response_class = HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "title": "dashboard", "peers": peers_db}
    )



if __name__ == "__main__":
    app.run("main:app", host="127.0.0.1", port=8000, reload=True)
