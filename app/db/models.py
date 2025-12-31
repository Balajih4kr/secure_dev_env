from sqlalchemy import Column, Integer, String
from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, index=True, primary_key=True)
    device_name = Column(String)
    origin_ip = Column(String)
    device_ip = Column(String)
    device_status = Column(String)