import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq, irfft

# defining the sample rate of the signal
SAMPLE_RATE = 44100  # hz
DURATION = 5
# Creating a Signal


def generateSinWave(frequency, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate*duration, endpoint=False)
    frequencies = x*frequency
    y = np.sin((2*np.pi)*frequencies)
    return x, y


# Adding signals together
_, tone = generateSinWave(400, SAMPLE_RATE, DURATION)
_, noise = generateSinWave(4000, SAMPLE_RATE, DURATION)

# x, y = generateSinWave(400, SAMPLE_RATE, DURATION)
# plt.title("Original Tone")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.plot(y[:1000])
# plt.show()


noise = noise * 0.3
# mixing noise
mixed = noise+tone

# normalization ,target format is a 16-bit integer, which has a range from -32768 to 32767 in which we store audio
normalized = np.int16((mixed / mixed.max())*32767)
# plt.title("Noisy Sine Wave")
# plt.plot(normalized[:1000])
# plt.show()
# outputting the written file
write("noiseysine.wav", SAMPLE_RATE, normalized)
# now we have sucessfully generated the audio now it's time to do FFT
N = SAMPLE_RATE*DURATION
#fft calculates both +ve and -ve half of frequency but rfft only calcualtes +ve half which makes it fastter than fft
yf = rfft(normalized)
xf = rfftfreq(N, 1/SAMPLE_RATE)


##Filtering the SIGnal

points_per_frequency = len(xf) / (SAMPLE_RATE/2)
#we want to eliminate 400hz signal
target = int(points_per_frequency*4000)

yf[target-1: target+2] = 0

# Now applying inverse fft
fresh_signal = irfft(yf)

#Now outputting clear sound 
normal_fresh = np.int16((fresh_signal / fresh_signal.max())* 32767 )
# plt.title("Fresh Sine Wave")
# plt.plot(normal_fresh[:1000])
# plt.show()
write("cleaned.wav", SAMPLE_RATE, normal_fresh)