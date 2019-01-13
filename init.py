import pyaudio
import numpy as np
import struct
import matplotlib.pyplot as plt
from scipy.fftpack import fft

print "START"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

#create matplotlib
fig, (ax, ax2) = plt.subplots(2, figsize = (15,7))

p = pyaudio.PyAudio()
print "streaming..."
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

#variable for plotting
x = np.arange(0, 2*CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

#line object
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK), '-', lw=2)
ax.set_ylim(0,400)
ax.set_xlim(0,2*CHUNK)
ax2.set_xlim(20,RATE/2)
plt.setp(ax, xticks=[0, CHUNK, 2*CHUNK], yticks=[0,128,255])
plt.show(block=False)
i = 1


while True:# i<=5:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(2*CHUNK)+'B',data)
    data_np = np.array((data_int), dtype='b')[::2] + 128
    # line.set_ydata(data_np)
    
    yf = fft(data_int)
    yfs = yf.argsort()
    yf_list = list(yfs)
    
    
    
    # print i
    # if i == 1:
    #     addingList = yf_list[5:]
    #     # print i, addingList
    # else:
    #     # print i
    #     for j in range(len(yf_list[5:])):
    #         addingList[j] += yf_list[j+5]
    #         # print "hi"
    #     if i == 5: 
    #         yuu = max(yf_list[5:])
    #         y_val = yf_list.index(yuu)
    #         print yuu, y_val#,yf_list
    #         # xf_list = list(x_fft[5:])
    #         # print len(xf_list)
    #         # x_val = xf_list[y_val]
    #         # print "poop"+str(x_val)
    #         i=0
    #         addingList = []
    #         # break
    #     # print i, addingList
    # # print "ok"
    # i += 1

    yuu = max(yf_list[5:])
    y_val = yf_list.index(yuu)
    print yuu, y_val
    
    
    # x1 = x_fft[order]
    # print "x:"+str(len(yf))
    # print "y:"+str(len(x_fft))
    # bro = np.interp(yoo, x_fft, yf)
    # tol = 1e-6;
    # bro = x_val(abs(order-yoo) < tol)

    line_fft.set_ydata(np.abs(yf[0:CHUNK])  / (128 * CHUNK))
    # print "Go!"
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        # print "Yay!"
    except:
        print('Stream stopped')
        break

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()