from sqlalchemy.orm import Session
from ..db import models

def assign_ip(db: Session):
    all_peers = db.query(models.Peer).all()

    assigned_ips = [peers.assigned_ips for peers in all_peers if peers.assigned_ips]
        for i in range(2, 255):
        candidate_ip = f"10.0.0.{i}"
        
        if candidate_ip not in assigned_ips:
            return candidate_ip
            
    return None




    


    
    


