from flask import Flask, request
from main import send_message

app = Flask(__name__)

@app.route('/notify', methods=['GET'])
def send_notification():
    return send_message()

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()