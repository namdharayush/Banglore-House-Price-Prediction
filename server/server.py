from flask import Flask,jsonify,request
from flask_cors import CORS
import util

util.load_saved_artifacts()
app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = str(request.form['location'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    get_price = util.get_estimated_price(location,total_sqft,bath, bhk)
    response = jsonify({
        'estimated_price' : get_price
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == '__main__':
    print("Starting the Python Flask Server....")
    app.run(host='0.0.0.0',port=5000)