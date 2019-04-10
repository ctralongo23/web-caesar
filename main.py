from flask import Flask, request
from caesar import encrypt


app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }

        </style>
    </head>
    <body>
        <form action="/caesar" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0"/>
            <textarea name="textarea"></textarea>
            <input type="submit"/>  
        </form>       
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/caesar", methods=['POST'])
def encrypt1():
    rot=int(request.form['rot'])
    textarea=request.form['textarea']
    return '<h1>'+encrypt(textarea, rot)+'</h1>'
    


app.run()

