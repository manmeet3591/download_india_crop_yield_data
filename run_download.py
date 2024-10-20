import datetime
from dateutil.relativedelta import relativedelta
import calendar
import os

dt = datetime.datetime(2009, 1, 1)
end = datetime.datetime(2019, 8, 31)

while dt < end:
    for i in range(1,23):
        dd_s = "%02d" % (dt.day,)
        mm_s = "%02d" % (dt.month,)
        yy_s = dt.year
        dd_e = calendar.monthrange(dt.year,dt.month)[1]
        mm_e = "%02d" % (dt.month,)
        yy_e = dt.year
        start_date = str(dd_s)+"/"+str(mm_s)+"/"+str(yy_s)
        end_date = str(dd_e)+"/"+str(mm_e)+"/"+str(yy_e)
        cmd = "python download.py "+start_date+" "+end_date+" "+str(i)
        print(cmd)
        try:
            os.system(cmd)
        except:
            pass
    dt = dt + relativedelta(months=+1)
