# -*- coding: utf-8 -*-
"""
web
~~~

:copyright: (c) 2017 by comwrg.
:license: MIT, see LICENSE for more details.
:time: 2017/08/17 19:27
"""

from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
