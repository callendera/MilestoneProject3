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
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#So they know how and where to run application