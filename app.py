# -*- coding: utf-8 -*-
"""
web
~~~

:copyright: (c) 2017 by comwrg.
:license: MIT, see LICENSE for more details.
:time: 2017/08/17 19:27
"""

import re

from flask import *

import _360ssp
import sys
sys.path.append('yundama')
from yundama import yundama

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    yuser = request.form['yuser']
    ypwd = request.form['ypwd']
    txt = request.files['txt']
    txt = deal(yuser, ypwd, txt.read().decode('utf-8'))
    return txt

def deal(yuser, ypwd, txt):
    y = yundama.Yundama(yuser, ypwd)
    lines = []
    for line in txt.split('\r\n'):
        try:
            u, p = line.strip().split('\t')
        except:
            continue
        u, p = u.strip(), p.strip()
        l = _360ssp._360ssp(u, p)
        r = l.verify()
        code = ''
        if r:
            cid = y.upload(r, 1000)
            code = y.result_loop(cid)
        r = l.login(code)
        lines.append('{user}\t{pwd}'.format(user=u, pwd=p))
        if not r:
            # login successful
            j = l.get_info()
            lines.append('网站名称\t审核状态\t封禁状态\t网站域名\t广告位数\t展示数\t点击数\t点击率\t预估收入')
            for item in j['result']:
                names = ('name_cn', 'status', 'forbid_status', 'website', 'adspacecnts', 'ns', 'nc', 'ctr', 'income')
                lnames = [filter_html(str(item[name])) for name in names]
                lines.append('\t'.join(lnames))
        else:
            # login failed
            lines.append('密码错误')
        lines.append('')
    return '\r\n'.join(lines)


def filter_html(s):
    """delete html code in `s`"""
    if not isinstance(s, str):
        return s
    for html in re.findall('<.*?>', s):
        s = s.replace(html, '')
    return s


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    # print(deal('comwrg', 'comwrg', '15005055930\tchen950611'))
