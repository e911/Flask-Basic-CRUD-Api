from flask import Blueprint, request, jsonify

from app.appointment.models import Appointment
from app.appointment.schemas import AppointmentSchema
from app.utils import custom_response

app = Blueprint('appointments', __name__,  url_prefix='/appointments')
appointments_schema = AppointmentSchema()


@app.route('/create_appointment', methods=['POST'])
def create():
    """
    Create an appointment
    """
    req_data = request.get_json()
    data, error = appointments_schema.load(req_data)
    if error:
        return jsonify(error), 400
    appointment = Appointment(data)
    appointment.save()
    data = appointments_schema.dump(appointment).data
    return custom_response(data, 201)


@app.route('/', methods=['GET'])
def get_all():
    """
    Get All Appointments
    """
    appointments = Appointment.get_all_appointments()
    data = appointments_schema.dump(appointments, many=True).data
    return custom_response(data, 200)


@app.route('/<int:appointment_id>', methods=['GET'])
def get_an_appointment(appointment_id):
    """
    Get An Appointments
    """
    appointment = Appointment.get_one_appointment(appointment_id)
    if not appointment:
        return custom_response({'Error': 'Appointment not found'}, 404)
    data = appointments_schema.dump(appointment).data
    return custom_response(data, 200)


@app.route('/<int:appointment_id>', methods=['PUT'])
def update(appointment_id):
    """
    Update An Appointment
    """
    req_data = request.get_json()
    appointment = Appointment.get_one_appointment(appointment_id)
    if not appointment:
        return custom_response({'Error': 'Appointment not found'}, 404)

    data, error = appointments_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    appointment.update(data)

    data = appointments_schema.dump(appointment).data
    return custom_response(data, 200)


@app.route('/<int:appointment_id>', methods=['DELETE'])
def delete(appointment_id):
    """
    Delete An Appointment
    """
    appointment = Appointment.get_one_appointment(appointment_id)
    if not appointment:
        return custom_response({'Error': 'Appointment not found'}, 404)

    appointment.delete()
    return custom_response({'Message': 'Appointment deleted'}, 204)
