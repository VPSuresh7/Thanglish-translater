
from flask import Flask, request, jsonify
import Py_Thanglish as py
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")  
def home():
    return "Hello you are in Thanglish translater!!" 

@app.post('/translate')
@cross_origin(supports_credentials=True)
def translate():
    data = request.get_json()
    input = data["text"]
    output = py.tamil_to_thanglish(input)
    return jsonify({"response":output}),200 
