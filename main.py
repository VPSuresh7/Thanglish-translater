
from flask import Flask, request, jsonify
import Py_Thanglish as py
app = Flask(__name__)


@app.route("/")  
def home():
    return "Hello you are in Thanglish translater!!" 

@app.post('/translate')
def translate():
    data = request.get_json()
    input = data["text"]
    output = py.tamil_to_thanglish(input)
    return jsonify({"response":output}),200 
