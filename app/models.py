from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import datetime

db = SQLAlchemy()


@dataclass
class CTD(db.Model):
    id: int
    cruise: str
    station: str
    type: str
    datetime: datetime
    lat: float
    lon: float
    depth: float
    temperature: float
    transmission: float
    par: str
    fluorescence: float
    density: float
    oxygen: float
    salinity: float
    turbidity: float

    __tablename__ = "CTD_Data"
    id = db.Column(db.Integer, primary_key=True)
    cruise = db.Column(db.String())
    station = db.Column(db.String(10))
    type = db.Column(db.String(10))
    datetime = db.Column(db.DateTime)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    depth = db.Column(db.Float)
    temperature = db.Column(db.Float)
    transmission = db.Column(db.String())
    par = db.Column(db.String())
    fluorescence = db.Column(db.Float)
    density = db.Column(db.Float)
    oxygen = db.Column(db.Float)
    salinity = db.Column(db.Float)
    turbidity = db.Column(db.Float)

    def __repr__(self):
        return f"<CTD: {self.cruise}-{self.station}-{self.datetime}>"
