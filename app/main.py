from flask import Flask, send_file
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Seattle Build 2017! This is Python 3.5 using Flask Web App on Linux"

@app.route("/index")
def main():
    return send_file('./static/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
