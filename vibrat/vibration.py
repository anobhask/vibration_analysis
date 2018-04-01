import os
import serial
import time
import matplotlib.pyplot as plt
import numpy as np

port = raw_input("Enter Port Address : ")
data = serial.Serial( port , baudrate=9600 , timeout=1 )

h = time.localtime()
h = str(h[2]) + '-' + str(h[1]) + '-' + str(h[0])
print(h)

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
            print ("Waiting for data.....")
        else:
            for i in range(int(samples)):
                
                print (data.readline())
                file.write(data.readline() + '\n')

            
                if i == samples:
                    file.close()
            break
                
def data_2_graph():
    try:    
        os.chdir('C:\\Users\\OriGin\\Desktop\\vibrat')
        folder = input("Enter date of Ploted data Eg : \"01-01-2017\" :")
        os.chdir(folder)
        file = input("Enter file name to plot graph : ")
        data = np.loadtxt(file+'.txt')

        x = []
        y = []
        z = []

        for dat in data:

            x.append(dat[0])
            y.append(dat[1])
            z.append(dat[2])

        plt.plot(x, 'r')
        plt.plot(y, 'g')
        plt.plot(z, 'b')

        plt.title('Ploted Vibration')

        plt.pause(0.001)
        plt.ylabel('Vibration ->')
        plt.xlabel('Time in sec ->')

        #plt.ylim(200,300)
        plt.show()
            
    except:
        print ("Error")
        pass

while True:

    print ("Chose your options : ")
    print ("1 Create Data Base ")
    print ("2 Plot graph from Data Base ")
    print ("3 Exit")

    choice = input("Your Choice : ")
    if (choice == '1'):
        data_2_text()
    elif (choice == '2'):
        data_2_graph()
    elif (choice == '3'):
        break;











