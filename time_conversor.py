import time
from datetime import datetime
class TimeConversor():

    def __init__(self):
         pass

    def getTimeStamp(dateTimeValue):
         current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         new = str(dateTimeValue)[0:10]
         current= str(current)[0:10]
         if new > current:
             format_date = datetime.strptime(str(dateTimeValue)[:-7], '%Y-%m-%d %H:%M:%S').timetuple()
             return time.mktime(format_date)
         else:
              return float(0)
        
         
         
         

