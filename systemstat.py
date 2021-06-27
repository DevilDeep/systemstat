import psutil



def checktemp():
    return psutil.sensors_temperatures()

def cpunum():
    return psutil.cpu_count()