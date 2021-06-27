import psutil



def checktemp():
    return psutil.sensors_temperatures()

def cpunum():
    return psutil.cpu_count()

def getnetaddrs():
    return psutil.net_if_addrs()
 
def getbatterydata():
    return psutil.sensors_battery()

def getfandata():
    return psutil.sensors_fans()