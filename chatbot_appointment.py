from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demo purposes
appointments = []

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    if 'book' in user_input.lower() or 'appointment' in user_input.lower():
        return jsonify({"response": "Sure, I can help with that. Please provide your name and preferred date/time."})

    if any(keyword in user_input.lower() for keyword in ['my name is', 'schedule for']):
        appointments.append(user_input)
        return jsonify({"response": "Your appointment has been booked. Thank you!"})

    return jsonify({"response": "Hi! I'm your assistant. I can help book appointments. Just say 'book an appointment'."})

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(debug=True)
