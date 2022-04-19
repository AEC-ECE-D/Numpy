# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:21:11 2022

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
Variable1=9
Variable2=2
a_c= 2+.25*Variable1
f_c= 50+.5*Variable1
a_m=2+.25* Variable2
f_m= 10+.25*Variable2
modulation_index=0.5
N=600
T=1.0/800.0
t= np.linspace(0.0,N*T,N)
carrier=a_c*np.cos(2*np.pi*f_c*t)
message=a_m*np.cos(2*np.pi*f_m*t)
modulated=a_c*(1+modulation_index*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)
plt.figure()
plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(message,'g') 
plt.ylabel('Amplitude ') 
plt.xlabel('Message signal')
plt.subplot(3,1,2)
plt.plot(carrier, 'r')
plt.ylabel('Amplitude') 
plt.xlabel('Carrier signal')
plt.subplot(3,1,3)
plt.plot(modulated, color="purple") 
plt.ylabel('Amplitude') 
plt.xlabel('AM signal')
plt.subplots_adjust(hspace= 1)
plt.rc('font', size=15)
fig = plt.gcf() 
fig.set_size_inches(16, 9)
plt.suptitle('Time Domain Plotting') 
fig.savefig('21a95a0428.png', dpi=100)
carrier_Freq = np.fft.fft(carrier) 
message_Freq = np.fft.fft(message) 
modulated_Freq = np.fft.fft(modulated)
freq = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
plt.figure(2) 
plt.subplot(3,1,1) 
plt.title('Message signal')
plt.plot(freq, 2.0/N * np.abs(message_Freq[0:int (N/2)])) 
plt.xlim([0,100])
plt.grid() 
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.subplot(3,1,2)
plt.plot(freq,2.0/N*np.abs(carrier_Freq[0:int(N/2)])) 
plt.xlim([0,100])
plt.grid()
plt.title('Carrier signal') 
plt.ylabel('Arnplitude') 
plt.xlabel('Frequency')
plt.subplot(3,1,3)
plt.plot(freq, 2.0/N * np.abs(modulated_Freq[0:int(N/2)])) 
plt.xlim([0, 100 ])
plt.grid()
plt.title('Modulated signal') 
plt.ylabel('Amplitude') 
plt.xlabel('Frequency')
plt.suptitle('Frequency Domain Plotting')
plt.subplots_adjust(hspace=1) 
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(  6, 9) 
plt.show()
fig.savefig('Spectrum_21a95a0428.png', dpi=100)