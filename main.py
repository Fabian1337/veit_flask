#!/usr/bin/env python
import datetime
import itertools
import time
from flask import Flask, Response, redirect, request, url_for
from timer import TimerClass
from timer import Reset
app = Flask(__name__)
reset = False

# @app.route('/time')
# def timestream():
#     timehandler = TimerClass()
#     if request.headers.get('accept') == 'text/event-stream':
#         def events():
#             for i, c in enumerate(itertools.cycle('\|/-')):
#                 yield "data: %s %s\n\n" % (c, timehandler.getCount())
#                 time.sleep(.1)  # an artificial delay
#         return Response(events(), content_type='text/event-stream')

@app.route('/resetbutton')
def resetbutton():
    reset = Reset()
    reset.setReset(True)
    return "Test redirect & url_for"



@app.route('/resetstream')
def resetstream():
    reset = Reset()
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                yield "data: %s %s\n\n" % (c, reset.getReset())
                time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.run(host='localhost', port=8080)
