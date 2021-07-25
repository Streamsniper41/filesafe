from flask import Flask
import os, sys
from flask import render_template_string
from flask import redirect
from flask import request
import subprocess
import subprocess
import shutil
app = Flask(__name__)
# HTML PAGE
@app.route('/')
def root():
    return render_template_string('''
        <html>
          <head>
            <title>File Vault</title>
          </head>
          <body>
            <div align="center">
              <h1>File Vault</h1>
              <p><strong>CWD: </strong>{{ current_working_directory[38:] }}</p>
            </div>
            
            
            <ul>
             <form action="/touch">
                <input type="submit" value="New file"/>
                <input name="filename" type="text" value="new_file.txt"/>
              </form>

              <form action="/md">
                <input type="submit" value="New folder"/>
                <input name="folder" type="text" value="new_folder"/>
              </form>
              <li><a href="/cd?path=..">..</a></li>
              {% for item in file_list[0: -1] %}
                {% if '.' not in item%}
                  <li><strong><a href="/cd?path={{current_working_directory + '/' + item}}">{{item}}</a></strong><a href="/rm?dir={{item}}"> X</a></li>
                {% elif '.txt' in item or '.py' in item or '.json' in item or '.html' in item %}
                  <li><strong><a href="/view?file={{current_working_directory + '/' + item}}">{{item}}</a></strong></li>
                {% else %}
                  <li>{{item}}</li>
                {% endif%}
              {% endfor %}
            </ul>
          </body>
        </html>
    ''', current_working_directory=os.getcwd(),
         file_list=subprocess.check_output('ls', shell=True).decode('utf-8').split('\n')) # use 'dir' command on Windows
    
# handle 'cd' command
@app.route('/cd')
def cd():
    # run 'level up' command
    os.chdir(request.args.get('path'))
    
    # redirect to file manager
    return redirect('/')

# handle 'make directory' command
@app.route('/md')
def md():
    # create new folder
    os.mkdir(request.args.get('folder'))
    
    # redirect to file manager
    return redirect('/')

    # handale 'make file' command
@app.route('/touch')
def touch():
    # create file 
    open(request.args.get('filename'), 'a+').close()
    #redirect to file manager
    return redirect('/')


# handle 'make directory' command
@app.route('/rm')
def rm():
    # remove certain directory
    shutil.rmtree(os.getcwd() + '/' + request.args.get('dir'))
    
    # redirect to fole manager
    return redirect('/')
    
# view text files
@app.route('/view')
def view():
    # get the file content
    with open(request.args.get('file')) as f:
        return f.read().replace('\n', '<br>')



# @app.route("/1")
# def test():
#     f = open('test.txt', 'r')
#     f_content = f.read()
#     return f_content
#     f.close()    


# # getfiles function: gets list of files in database and returns them to the client 
# @app.route("/getfiles")
# def getfiles():
#    return f"{os.listdir(path='DB/')}"


# download file from database 
@app.route('/uploads/<path>', methods=['GET', 'POST'])
def download(path):
    return f"hello {path}!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)





