# Import flask from the Flask library
from flask import Flask, render_template, request, session
from flask_session import Session

# Import the translation function
from translate import detect, translate

# Import the dpla search
from dpla import dpla

# Use CSV reader to read in Amazon Listings
import csv

# Create a Flask object and pass in __name__
app = Flask(__name__)

# Configure session
app.config["SESSION PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

DATABASE = [
    "All", "Dpla", "Amazon Listings", "Europana"
]

LANGUAGES = {
    'ar': 'Arabic',
    'cs': 'Czech',
    'de': 'German',
    'el': 'Greek',
    'es': 'Spanish',
    'fr': 'French',
    'ga': 'Irish',
    'he': 'Hebrew',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ms': 'Malay',
    'ru': 'Russian',
    'sw': 'Swahili',
    'ur': 'Urdu',
    'zh-CN': 'Chinese'
}

# Set the url ending, this is a root path
@app.route('/')
def greet():
    return render_template("greet.html")

@app.route('/select')
def select():
    return render_template("select.html", database=DATABASE)

@app.route('/language')
def language():
    name = request.args.get("name")
    database = request.args.get("database")
    session["name"] = name
    session["database"] = database

    langauge = detect(name).lang
    output = []

    for key in LANGUAGES:
        temp = dict()
        temp['language'] = LANGUAGES[key]
        temp['text'] = translate(dest=key, string=name).text
        output.append(temp)

    return render_template("language.html", name=name, database=database,
                           langauge=langauge, output=output)

@app.route('/result')
def result():
    name = session.get("name")
    database = session.get("database")

    dpla_data = dpla(tosearch=name)
    return render_template("result.html", name=name, database=database, dpla_data=dpla_data)

@app.route('/amazon')
def amazon():
    with open("images.txt", 'r') as f:
        content_list = f.readlines()
        content_list = content_list[0].replace("[", "").replace("]","").\
            replace("src=", "").replace('"', '').replace("'","").split(",")
    return render_template('amazon.html', dress=content_list)

if __name__ == '__main__':
    app.run()






