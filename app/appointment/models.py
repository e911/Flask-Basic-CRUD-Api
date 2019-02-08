from datetime import datetime
from .. import db


class Appointment(db.Model):
    """
    Appointment Model
    """
    __tablename__ = 'appointments'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(128), nullable=False)
    request_date = db.Column(db.Date(), nullable=False)
    appointment_date = db.Column(db.Date(), nullable=False)
    appointment_time = db.Column(db.Time(), nullable=False)
    preferred_clinician = db.Column(db.String(128), nullable=False)
    appointment_reason = db.Column(db.String(300), nullable=False)

    def __init__(self, data):
        self.client_name = data.get('client_name')
        self.request_date = datetime.now().date() or data.get('request_date')
        self.appointment_date = data.get('appointment_date') or datetime.now().date()
        self.appointment_time = data.get('appointment_time') or datetime.now().time()
        self.preferred_clinician = data.get('preferred_clinician')
        self.appointment_reason = data.get('appointment_reason')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_appointments():
        return Appointment.query.all()

    @staticmethod
    def get_one_appointment(id):
        return Appointment.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)
