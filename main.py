from flask import Flask, request
from caesar import encrypt


app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
             @import url('https://fonts.googleapis.com/css?family=Crafty+Girls');
        </style>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

            .background{{
                background:purple;
            }}

            .dude{{
                 display: block;
                margin-left: auto;
                margin-right: auto;
                width: 15%;
                padding-top:20px;
            }}

            .title{{
                text-align:center;
                font-family: 'Crafty Girls', cursive;
                font-size:90px;
                font-weight:bold;
            }}

        </style>
        <div class="title">Web Caesar</div>
    </head>
    <body class="background">
        <form action="/" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0"/>
            <textarea name="textarea">{0}</textarea>
            <input type="submit" value="Push Me"/>
        </form>       
         <img src="https://upload.wikimedia.org/wikipedia/commons/4/48/0092_-_Wien_-_Kunsthistorisches_Museum_-_Gaius_Julius_Caesar.jpg" class="dude"/>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt1():
    rot=int(request.form['rot'])
    textarea=request.form['textarea']
    return form.format(encrypt(textarea, rot))    


app.run()

