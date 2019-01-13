import pyaudio
import numpy as np
import struct
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

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


fig, ax = plt.subplots()
x = np.arange(0, 2*CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
# x = 0
while True:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2*CHUNK)+'B',data), dtype='b')[::2] + 128
    line.set_ydata(data_int)
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
        
    except TclError:
        
        # calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)
        
        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    # x+=1
# ax.plot(data_int,'-')
# plt.show()