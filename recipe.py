import os
from flask import Flask
#sets up application for use with flask functionality

app = Flask(__name__)
#creates application to be tested


@app.route('/')
#Display text as proof of concept
def fromscratch():
    return "FROM Scratch test"


if __name__ == '__main__':
    app.run(debug=True)
#So they know how and where to run application