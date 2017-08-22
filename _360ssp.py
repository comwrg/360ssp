# -*- coding: utf-8 -*-
"""

~
:time: 2017/08/18 14:34
:copyright: (c) 2017 by comwrg.
:license: MIT, see LICENSE for more details.
"""

import sys
sys.path.append('360login')
from _360login._360 import _360
from datetime import datetime, timedelta
class _360ssp(_360):
    def get_info_yesterday(self):
        yesterday = datetime.now() - timedelta(days=1)
        r = self._session.get('http://ssp.360.cn/pub/site/view?type=list&page=1&size=200&startDate={yesterday}&endDate={yesterday}&dateGroupType=&disabled=undefined&sortOrder=desc&sortName='
                              .format(yesterday=yesterday.strftime('%Y-%m-%d')))
        return r.json()
