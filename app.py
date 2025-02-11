from flask import Flask, request, jsonify
from salary_processer import start_processing
from config import logging


app = Flask(__name__)

@app.route('/process-json', methods=['POST'])
def process_json():

    

    try:
        # Get JSON data from request if in json
        if request.is_json:
            content = request.get_json()
        else:
            return jsonify({'error':'Data not in correct format'}), 500
        logging.info("Recieved request as: {0}".format(content))

        # Check if data exists
        if not content:
            return jsonify({'error': 'No JSON data received'}), 400
        
        response_data = start_processing(content)

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/health', methods=['GET'])
def get_health():

    data = 'I am Healthy'
    
    response_data = {
        "Health": data,
    }

    return jsonify(response_data), 200
    

if __name__ == '__main__':
    app.run(debug=True)
