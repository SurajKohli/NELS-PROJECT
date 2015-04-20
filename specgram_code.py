from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy

def specgram_calc( framesize , sampling_freq , overlap):
    fsamp = int(frame_size * sampling_freq)
    osamp = int(overlap * sampling_freq)
    win = numpy.hamming( fsamp )  #windowing function
    #here Pxx is len(times) X len(freqs) array of power
    #im is matplotlib.image.AxesImage
    ( Pxx , freqs , timepoints , im ) = plt.specgram( numpy.array(filedata) , NFFT=fsamp , Fs=sampling_freq , window=win , noverlap=osamp)


myfile = raw_input("Enter filename:  ")
rate , filedata = wavfile.read( myfile )
frame_size =  input("Enter framesize: ")
sampling_freq = input("Enter sampling frequency: ")
overlap = input("Enter overlap: ")

#plotting spectrogram using specgram function call
data = specgram_calc(frame_size, sampling_freq ,overlap)

#plt.plot(numpy.array(data))
plt.show()

