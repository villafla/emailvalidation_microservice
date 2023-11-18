from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    data = request.get_json()
    email = data.get('email')

    is_valid = validate_email_function(email)

    response_data = {
        'email': email,
        'is_valid': is_valid
    }

    return jsonify(response_data)

def validate_email_function(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    app.run(debug=True)
