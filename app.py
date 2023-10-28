#from crypt import methods
from flask import Flask, render_template, request, redirect
from firebase_admin import firestore
#jika tidak pakai web gui
#from os import path
import calendar
import time
import flaskwebgui
from flaskwebgui import FlaskUI


#jika tidak pakai web GUI
#basedir = path.abspath(path.dirname(__file__))
#config = path.join(basedir, 'config/config.py')
app = Flask(__name__, template_folder="templates")
app.config.from_pyfile('config/config.py')
#db = firestore.client()
# tidak berguna gui = flaskwebgui.FlaskUI(app=app)
db = firestore.client()

@app.route('/', methods = ['POST', 'GET'])
def index():
    docs = db.collection('taskList').order_by('id', direction=firestore.Query.DESCENDING).get()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    print(data)
    return render_template("Home.html", tasks = data)

@app.route("/addToList", methods =['POST', 'GET'])
def addToList():
    if request.method == 'POST':
        todo = request.form.get('todo')
        id = str(calendar.timegm(time.gmtime()))
        db.collection('taskList').document(f'{id}').set({ 'id' : id, 'data' : todo })
        
        return redirect('/')

@app.route("/delete/<int:id>")
def delete(id):
    db.collection('taskList').document(f'{id}').delete()
    return redirect ('/')

if __name__ == '__main__':
    #app.run(debug=True)
    FlaskUI(app=app, server="flask").run()

#python3 -m venv env 
#install flask flaskwebgui pyinstaller firebase-admin
#install env
#pip freeze
#pip freeze > requirements.txt
# jika powershell bermasalah https://stackoverflow.com/questions/57673913/vsc-powershell-after-npm-updating-packages-ps1-cannot-be-loaded-because-runnin
#install node js
#npm install -g yarn
# buat package.json yarn init
#tailwind install di #yarn add -D tailwindcss
# yarn tailwindcss init
#yarn tailwindcss -i ./static/src/css/input.css -o ./static/dist/css/style.css --watch
#"scripts" : {
#    "watch": "yarn tailwindcss -i ./static/src/css/input.css -o ./static/dist/css/style.css --watch" 
#  }