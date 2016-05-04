#! user/bin/python
from datetime import datetime, timedelta
def giga():
    return timedelta(0, 10**9)
now = datetime.now()
print "%s %s %s"% (now.year, now.month, now.day)
print now + timedelta(0,10**9)


