from flask import Flask
import os

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1")
def test():
    f = open('test.txt', 'r')
    f_content = f.read()
    return f_content
    f.close()
# getfiles function: gets list of files in database and returns them to the client 

# @app.route("/getfiles")
# def getfiles():

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)