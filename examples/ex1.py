import time
import logging

from flask import Flask
from flask_urltimer import FlaskUrltimer, add_timemark, log as flask_urltimer_logger

logging.basicConfig(level=logging.INFO)
flask_urltimer_logger.level = logging.DEBUG

app = Flask(__name__)
urltimer = FlaskUrltimer(app)


@app.get('/first')
def first():
    sum = 0
    for i in range(100):
        sum += 1

    add_timemark('After sum')
    time.sleep(0.5)
    add_timemark('After sleep')

    for i in range(1000):
        sum += 1
    return 'Hello from First!'


if __name__ == '__main__':
    app.run(debug=True)
