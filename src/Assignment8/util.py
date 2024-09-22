from datetime import datetime

def delta():

    timestamp1 = "2024-09-22 15:00:00 +0530"  # Indian Standard Time (IST)
    timestamp2 = "2024-09-22 07:30:00 +0000"  # Coordinated Universal Time (UTC)


    time1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S %z")
    time2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S %z")


    time_difference = abs(time1 - time2)


    return time_difference

