from flask import Flask,request
import json
app1 = Flask(__name__)

@app1.route("/")
def home():
    return 'Web app 1'

if __name__ == '__main__':
    app1.run(host='0.0.0.0', debug=True, port=9000)
    