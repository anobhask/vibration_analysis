import os
import serial
import time
import matplotlib.pyplot as plt
import numpy as np

port = raw_input("Enter Port Address : ")
data = serial.Serial( port , baudrate=9600 , timeout=1 )

h = time.localtime()
h = str(h[2]) + '-' + str(h[1]) + '-' + str(h[0])
print h

os.chdir('C:\Users\LENOVO\Desktop\vibration')

#os.mkdir(h)
#os.chdir(h)

try:
    os.mkdir(h)
    os.chdir(h)

except:
    os.chdir(h)
    pass

def data_2_text():
    global sample
    file_Name = raw_input ("Enter motor serial number : ")
    samples = raw_input ("Enter number of samples required \"Maximum 1000 samples\": ")
    file = open(file_Name+'.txt','wb')
    while 1:
        if not data.readline():
            print "Waiting for data....."
        else:
            for i in range(int(samples)):
                
                print data.readline()
                file.write(data.readline() + '\n')

            
                if i == samples:
                    file.close()
            break
                
