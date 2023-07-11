import time
from datetime import datetime
class TimeConversor():

    def __init__(self):
         pass

    def getTimeStamp(dateTimeValue):
         
         format_date = datetime.strptime(str(dateTimeValue)[:-7], '%Y-%m-%d %H:%M:%S').timetuple()
         tt = time.mktime(format_date)
         print(str(tt))
         
         
         

