#!/usr/bin/env python3
from flask import Flask, jsonify, render_template, request
import schemepy.reader as rd
import schemepy.evaluator as ev


DEBUG = True
SECRET_KEY = '$(secret_key)'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/_interpret')
def add_numbers():
    statement = request.args.get('statement')
    expression = rd.parse(statement)
    res = ev.evaluate(expression)
    return jsonify(result= str(res))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
