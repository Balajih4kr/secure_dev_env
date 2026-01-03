import uvicorn
from fastapi import FastAPI, Request, Form, Depends
from wg.utils import assign_ip
from fastapi.responses import HTMLResponse, RedirectResponse
#from fastapi.staticfiles import staticfiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import engine, get_db
from db import models


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")




@app.post("/peers/create")
async def create_peer(
    developer_name: str = Form(...),
    device_name: str = Form(...),
    public_key: str = Form(...),
    db: Session = Depends(get_db)
):


    
    assigned_ip = assign_ip(db)
    
    if assigned_ip is None:
        
        return {"error": "No available IP addresses in the subnet."}

    new_peer = models.Peer(
        developer_name=developer_name,
        device_name=device_name,
        public_key=public_key.strip(),
        assigned_ip=f"{assigned_ip}/32", 
        status="Offline"
    )

    db.add(new_peer)
    db.commit()
    db.refresh(new_peer)

    
    return RedirectResponse(url="/", status_code=303)



@app.get('/', response_class = HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    peers_from_db = db.query(models.Peer).all()

    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "title": "dashboard", "peers": peers_from_db}
    )



if __name__ == "__main__":
    app.run("main:app", host="127.0.0.1", port=8000, reload=True)
