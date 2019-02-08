from flask_io import fields, Schema


class AppointmentSchema(Schema):
    """
    Appointment Schema
    """

    id = fields.Integer(dump_only=True)
    client_name = fields.String(required=True)
    request_date = fields.Date(required=False)
    appointment_date = fields.Date(required=False)
    appointment_time = fields.Time(required=False)
    preferred_clinician = fields.String(required=True)
    appointment_reason = fields.String(required=True)

