# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:25:54 2020

@author: DIXITA
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run()