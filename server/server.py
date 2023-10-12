from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS

# Your existing route definitions


@app.route('/get_location_names')
def get_location_names():
    locations = request.args.get('locations', None)
    print("Received locations parameter:", locations)  # Add this line for debugging

    if locations is not None:
        # If 'locations' is provided, return the corresponding data
        response = jsonify({
            'locations': util.get_location_names()
        })
    else:
        # If 'locations' is not provided, return an error response
        response = jsonify({
            'error': 'Location parameter is missing or null'
        })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        locations = request.form['locations']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(locations, total_sqft, bhk, bath)
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except (KeyError, ValueError) as e:
        # Handle missing or incorrect parameters
        error_message = f"Bad Request: {str(e)}"
        response = jsonify({
            'error': error_message
        })
        response.status_code = 400  # Set a 400 status code for a bad request
        return response

if __name__=="__main__":

    print("Starting Python Flask Server for Home Price Prediction...")
    app.run()