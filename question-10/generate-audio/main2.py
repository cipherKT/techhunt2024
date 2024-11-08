import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
duration = 5
amplitude = 0.5
morse_code = ".- -... -.-."

noise_base = np.random.uniform(-amplitude, amplitude, int(duration * sample_rate))

dot_duration = 0.1
dash_duration = 0.3
gap_duration = 0.1
space_duration = 0.3

def morse_to_amplitude_pattern(morse_code, sample_rate, dot_duration, dash_duration, gap_duration, space_duration):
    morse_pattern = []
    for symbol in morse_code:
        if symbol == '.':
            morse_pattern.extend([1] * int(dot_duration * sample_rate))
        elif symbol == '-':
            morse_pattern.extend([1] * int(dash_duration * sample_rate))
        elif symbol == ' ':
            morse_pattern.extend([0] * int(space_duration * sample_rate))
        morse_pattern.extend([0] * int(gap_duration * sample_rate))
    return np.array(morse_pattern)

morse_amplitude = morse_to_amplitude_pattern(morse_code, sample_rate, dot_duration, dash_duration, gap_duration, space_duration)
modulation = np.zeros(len(noise_base))
modulation[:len(morse_amplitude)] = morse_amplitude

noise1 = noise_base
noise2 = -noise_base

noise1 += np.random.uniform(-amplitude*0.1, amplitude*0.1, len(noise1))
noise2 += np.random.uniform(-amplitude*0.1, amplitude*0.1, len(noise2))

# Add the message to only one file with very small amplitude
noise2 += modulation * amplitude * 0.05

def save_wav(filename, data, sample_rate):
    data_normalized = np.int16(data / np.max(np.abs(data)) * 32767)
    write(filename, sample_rate, data_normalized)

save_wav("noise1.wav", noise1, sample_rate)
save_wav("noise2.wav", noise2, sample_rate)
save_wav("combined.wav", noise1 + noise2, sample_rate)