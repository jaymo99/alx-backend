#!/usr/bin/env python3
"""
Creates a flask application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Hello World page."""
    return render_template('0-index.html')
