from datetime import datetime

from app import db


class Json(db.Model):
    __tablename__ = 'jsons'

    id = db.Column(db.Integer, primary_key=True)
    sensor_type = db.Column(db.Integer, nullable=False)
    num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255))
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)

    timestamp_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.sensor_type

    def __repr__(self):
        return "<{}:{}>".format(id, self.sensor_type)
