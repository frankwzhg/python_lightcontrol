import serial
import time
from time import gmtime, strftime
import numpy as np
import pandas as pd

ser = serial.Serial('/dev/ttyACM0', 9600)
data = []
# time.sleep(20)
now = time.time()
future = now + 60
while time.time()<future:
    # time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    # abc = [time_now, ]
    serial_data = ser.readline()
    data.append(serial_data.rstrip())
    # data.append(abc)
print data

data_frame = pd.DataFrame(data)

print data_frame
