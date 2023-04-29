from flask import Flask, request, jsonify

# app = Flask(__name__)


# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, jsonify


app = Flask(__name__)

data = [
        {
            "id": 1,
            "frameworks": "Django",
            "year": 2005
        },
        {
            "id": 2,
            "frameworks": "Flask",
            "year": 2010
        },
        {
            "id": 3,
            "frameworks": "Web2Py",
            "year": 2007
        }
    ]

flight_details = [{'flight_id': 'VZ220', 'airline_name': 'Thai Vietjet Air', 'day': 'Wednesday', 'departure_date': None, 'departure_time': '10:30', 'arrival_date': None, 'arrival_time': '11:35', 'departure_airport': 'BKK', 'arrival_airport': 'UBP', 'cabin_baggage': 7, 'refund': False, 'reschedule': True, 'status': 'One Way'}, {'flight_id': 'VZ224', 'airline_name': 'Thai Vietjet Air', 'day': 'Wednesday', 'departure_date': None, 'departure_time': '15:00', 'arrival_date': None, 'arrival_time': '16:05', 'departure_airport': 'BKK', 'arrival_airport': 'UBP', 'cabin_baggage': 7, 'refund': False, 'reschedule': True, 'status': 'One Way'}, {'flight_id': 'WE20', 'airline_name': 'Thai Smile Air', 'day': 'Wednesday', 'departure_date': None, 'departure_time': '07:05', 'arrival_date': None, 'arrival_time': '08:15', 'departure_airport': 'BKK', 'arrival_airport': 'UBP', 'cabin_baggage': 20, 'refund': False, 'reschedule': True, 'status': 'One Way'}, {'flight_id': 'WE28', 'airline_name': 'Thai Smile Air', 'day': 'Wednesday', 'departure_date': None, 'departure_time': '16:15', 'arrival_date': None, 'arrival_time': '17:25', 'departure_airport': 'BKK', 'arrival_airport': 'UBP', 'cabin_baggage': 20, 'refund': False, 'reschedule': True, 'status': 'One Way'}]

@app.route('/flight_details/<flight_id>', methods=['GET'])
def get_flight_details(flight_id):
    for flight in flight_details:
        if flight['flight_id'] == flight_id:
            return jsonify(flight)
    return jsonify({'message': 'Flight not found'})

@app.route('/')
def home():
    return "Hello World"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)  # Return web frameworks information


if __name__ == "__main__":
    app.run(debug=True)