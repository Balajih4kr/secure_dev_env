from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Peer(Base):
    __tablename__ = "peers"

    id = Column(Integer, primary_key=True, index=True)
    developer_name = Column(String, index=True)
    device_name = Column(String)
    public_key = Column(String, unique=True, index=True)
    assigned_ip = Column(String, unique=True)
    status = Column(String, default="Offline")
    created_at = Column(DateTime, default=datetime.utcnow)