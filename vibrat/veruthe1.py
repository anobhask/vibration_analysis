import serial
import os
import time
import matplotlib.pyplot as plt
import numpy as np
#from scipy.fftpack import fft
from statistics import mean

os.chdir('E:\\vibrat')
"""
port = input("Enter Port Address :")
data = serial.Serial(port , baudrate=9600 , timeout=1)  
print(data)
h = time.localtime()
h = str(h[2]) + '-' + str(h[1]) + '-' + str(h[0])
print(h)

os.chdir('E:\\vibrat')

#os.mkdir(h)
#os.chdir(h)

try:
    os.mkdir(h)
    os.chdir(h)

except:
    os.chdir(h)
    pass
"""
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
 
    os.chdir('E:\\vibrat')
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
        
    fig, ax = plt.subplots(3, 1)



    ax[0].set_title('Vibration in Time domain')

    #ax[0].set_pause(0.001)
    ax[0].set_ylabel('Vibration (x)->')
    ax[0].set_xlabel('Time in sec ->')
    ax[1].set_ylabel('Vibration (y)->')
    ax[1].set_xlabel('Time in sec ->')
    ax[2].set_ylabel('Vibration (z)->')
    ax[2].set_xlabel('Time in sec ->')
    ax[0].plot(x, 'r')
    ax[1].plot(y, 'g')
    ax[2].plot(z, 'b')

    plt.show()
    
    fig, ax = plt.subplots(3, 1)
    f = np.fft.fft(x)

    freq = np.fft.fftfreq(len(x))
    ax[0].plot(abs(f))
    ax[0].set_ylabel('Vibration ->')
    ax[0].set_xlabel('frequency in HZ ->')

    f1 = np.fft.fft(y)
    
    freq = np.fft.fftfreq(len(y))
    ax[1].plot(abs(f1)) 
    ax[1].set_ylabel('Vibration ->')
    ax[1].set_xlabel('frequency in HZ ->')
    #y3 = np.sin(2*np.pi*x)


    f2 = np.fft.fft(z)
    
    freq = np.fft.fftfreq(len(z))
    ax[2].plot(abs(f2)) 
    #ax[1].set_title('Ploted Vibration')
    
    plt.pause(0.001)
    ax[2].set_ylabel('Vibration ->')
    ax[2].set_xlabel('frequency in HZ ->')
    plt.show()


    ef=0;l=0;E_abs=0;
    Ex=[]
    for i in range(0,64):
        for k in range(0,8):
        #E.append(abs(f[i])**2)
            ef=ef+(abs(f[l])**2)
            l=l+1
        print("Values of len nd E:",l,ef)
        Ex.append(ef)
        ef=0

    ef=0;l=0;E_abs=0;
    Ey=[]
    for i in range(0,64):
        for k in range(0,8):
        #E.append(abs(f[i])**2)
            ef=ef+(abs(f[l])**2)
            l=l+1
        print("Values of len nd E:",l,ef)
        Ey.append(ef)
        ef=0

    ef=0;l=0;E_abs=0;
    Ez=[]
    for i in range(0,64):
        for k in range(0,8):
        #E.append(abs(f[i])**2)
            ef=ef+(abs(f[l])**2)
            l=l+1
        print("Values of len nd E:",l,ef)
        Ez.append(ef)
        ef=0
        

    #ef=ef/512
    #Ef=np.sum(f**2)/512;
    #print ("Ef = %.1f" % ef);
    #print(E)

    fig, ax = plt.subplots(3, 1)



    ax[0].set_title('Energy spectrum')

    #ax[0].set_pause(0.001)
    ax[0].set_ylabel('Energy ->')
    ax[0].set_xlabel('frequency in HZ ->')
    ax[1].set_ylabel('Energy ->')
    ax[1].set_xlabel('Tfrequency in HZ ->')
    ax[2].set_ylabel('Energy ->')
    ax[2].set_xlabel('frequency in HZ ->')
    ax[0].plot(Ex, 'r')
    ax[1].plot(Ey, 'g')
    ax[2].plot(Ez, 'b')
    #plt.plot(E) 
    #plt.plot(x, 'r')
    #plt.plot(y, 'g')
    #plt.plot(z, 'b')

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

