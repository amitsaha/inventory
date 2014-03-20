from sqlalchemy import Column, Integer, Text, String
from webapp.database import Base

class System(Base):

    __tablename__ = 'system'

    id = Column(Integer, primary_key=True)
    mac = Column(Text(), unique=True)
    cpuinfo = Column(Text())
    
    def __init__(self, mac, cpuinfo):
        self.mac = mac
        self.cpuinfo = cpuinfo

    def __repr__(self):
        return '<System %r>' % (self.mac)
