
from datetime import datetime

def calender_module(n):

    str_format=datetime.strptime(n,"%d %m %Y")

    res=datetime.strftime(str_format,"%A")

    return res
