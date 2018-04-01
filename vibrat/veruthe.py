import serial
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from statistics import mean


port = input("Enter Port Address :")
data = serial.Serial(port , baudrate=9600 , timeout=1)  
print(data)
h = time.localtime()
h = str(h[2]) + '-' + str(h[1]) + '-' + str(h[0])
print(h)

os.chdir('C:\\Users\\OriGin\\Desktop\\vibrat')

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
    file_Name = input ("Enter motor serial number : ")
    samples = input ("Enter number of samples required \"Maximum 1000 samples\": ")
    file = open(file_Name+'.txt','w')
    flag = 1
    while flag:
        if not data.readline():
            print ("Waiting for data.....")
        else:
            for i in range(int(samples)):
                print (i)
                print (samples)
                print (data.readline())
                read= data.readline()
                file.write(str(read.decode())+'\n')
        

            
                if i == int(samples)-1:
                    file.close()
                    flag = 0
                    break
def data_2_graph():
 
    os.chdir('C:\\Users\\OriGin\\Desktop\\vibrat')
    folder = input("Enter date of Ploted data Eg : \"01-01-2017\" :")
    os.chdir(folder)
    file = input("Enter file name to plot graph : ")
    data = np.loadtxt(file+'.txt')

    
    x = []
    y = []
    z = []
    d=[]
    e=[]
    f=[]
    for dat in data:

        x.append(dat[0])
        y.append(dat[1])
        z.append(dat[2])
    #y1 = np.sin(2*np.pi*x)
    l=mean(x)
    m=mean(y)
    n=mean(z)
    for a in x:
        d.append(a-l)
    for a in y:
        e.append(a-m)
    for a in z:
        f.append(a-n)
    print(d)
    print(e)
    print(f)
    x=d
    y=e
    z=f
        
    
    #n=len(x)
    f = np.fft.fft(x)
    #f=f[range(int(n/2))]
    print("value of f")
    print (f[1])
    freq = np.fft.fftfreq(len(x),(1/512))
    plt.plot(freq, abs(f))
    #plt.plot(abs(f))
    #y2 = np.sin(2*np.pi*x)
    print(freq)
    f1 = np.fft.fft(y)
    
    freq = np.fft.fftfreq(len(y))
    plt.plot(freq, abs(f1)) 

    #y3 = np.sin(2*np.pi*x)


    f2 = np.fft.fft(z)
    
    freq = np.fft.fftfreq(len(z))
    plt.plot(freq, abs(f2)) 

    #X=np.array([x])
    #X1= fft(X)
    #print(X1)
    #plt.plot(abs(X1))
    #Y=np.array([y])
    #Y1= fft(Y)
    #plt.plot(abs(Y1))
    #Z=np.array([z])
    #Z1= fft(Z)
    #plt.plot(abs(Z1))
    #plt.plot(x, 'r')
    #plt.plot(y, 'g')
    #plt.plot(z, 'b')

    plt.title('Ploted Vibration')
    
    plt.pause(0.001)
    plt.ylabel('Vibration ->')
    plt.xlabel('frequency in HZ ->')
    plt.show()
    ef=0;
    E=[]
    for i in range(0,512):
        E.append(abs(f[i])**2)
        ef=ef+E[i]
        print(f[0])
    ef=ef/512
    #Ef=np.sum(f**2)/512;
    print ("Ef = %.1f" % ef);
    print(E)
    plt.plot( E, abs(f)) 
    #plt.plot(x, 'r')
    #plt.plot(y, 'g')
    #plt.plot(z, 'b')

    plt.title('Ploted Energy spectrum')
    
    plt.pause(0.001)
    plt.ylabel('Energy ->')
    plt.xlabel('frequency in HZ ->')
    plt.show()
    
  
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

