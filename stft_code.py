from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy

def stft_calc(frame_size,sampling_freq,overlap):
    fsamp = int(frame_size * sampling_freq)
    osamp = int(overlap * sampling_freq)
    stft_data = []
    win = numpy.hamming( fsamp )  #windowing function

    for i in range(0,len(filedata) - fsamp,osamp):
        fft_data = numpy.fft.rfft(win * filedata[i:i+fsamp])
        stft_data.append(fft_data)
    return stft_data

myfile = raw_input("Enter filename:  ")
rate , filedata = wavfile.read( myfile )
frame_size =  input("Enter framesize: ")
sampling_freq = input("Enter sampling frequency: ")
overlap = input("Enter overlap: ")


data = stft_calc(frame_size,sampling_freq,overlap)

plt.plot(numpy.array(data))
#plt.specgram(numpy.array(stft_data))
plt.show()

