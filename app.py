from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# This is a placeholder API URL for prediction (use a real API in production)
PREDICTION_API_URL = "https://www.football-data.org/get_epl_predictions"  # Change this to a real API URL

# Route to serve the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch predictions for all EPL games
@app.route('/get_all_predictions', methods=['GET'])
def get_all_predictions():
    response = requests.get(PREDICTION_API_URL)
    predictions = response.json()  # Assuming the response is in JSON format
    return jsonify(predictions)

# Route to fetch predictions for the best 5 games
@app.route('/get_best_five_predictions', methods=['GET'])
def get_best_five_predictions():
    response = requests.get(PREDICTION_API_URL)
    predictions = response.json()
    
    # Sort or filter predictions based on likelihood
    best_five = sorted(predictions, key=lambda x: x['probability'], reverse=True)[:5]
    
    return jsonify(best_five)

if __name__ == '__main__':
    app.run(debug=True)
