import time
import logging

from flask import Flask
from flask_urltimer import FlaskUrltimer, add_timemark, log as flask_urltimer_logger, check_source

logging.basicConfig(level=logging.INFO)
flask_urltimer_logger.level = logging.DEBUG

app = Flask(__name__)
urltimer = FlaskUrltimer(app)


@app.get('/first')
@check_source
def first():
    sum = 0
    for i in range(10000):
        sum += 1

    add_timemark('After sum')
    time.sleep(0.5)
    add_timemark('After sleep')

    for i in range(10000):
        sum += 1
    return 'Hello from First!'


@app.get('/second')
@check_source
def second():
    time.sleep(0.3)
    add_timemark('Wake up')
    time.sleep(0.8)
    add_timemark(0.3)
    return 'Finish'


if __name__ == '__main__':
    app.run(debug=True)
