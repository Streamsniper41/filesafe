from flask import Flask
import os, sys
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
@app.route("/getfiles")
def getfiles():
   print(os.listdir(path='DB/'))
   return "yes"


# download file from database 
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['DB/'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)