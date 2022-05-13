import time
import logging

from flask import Flask
from flask_urltimer import FlaskUrltimer, log as flask_urltimer_logger

logging.basicConfig(level=logging.INFO)
flask_urltimer_logger.level = logging.DEBUG

app = Flask(__name__)
urltimer = FlaskUrltimer(app)


@app.get('/first')
def first():
    time.sleep(1)
    return 'Hello from First!'


if __name__ == '__main__':
    app.run(debug=True)
