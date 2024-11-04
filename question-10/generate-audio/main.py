import numpy as np
from scipy.io import wavfile


def generate_audio_files():
    # Audio parameters
    sample_rate = 44100
    duration = 10  # seconds

    # Calculate total samples
    total_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, total_samples)

    # Generate complex noise for file 1
    noise = np.zeros_like(t)
    for f in np.linspace(200, 2000, 30):
        noise += np.sin(2 * np.pi * f * t + np.random.random() * 2 * np.pi)

    # Create base signals with inverse noise
    signal1 = noise
    signal2 = -noise  # Inverse of signal1's noise

    print(signal1)
    print(signal2)

    # Morse code timing parameters
    dot_duration = 0.1
    dash_duration = 0.3
    space_duration = 0.1

    # Morse pattern for TMKC
    morse_pattern = [
        -1, 0,  # T (-)
        1, -1, 1, 0,  # R (.-.)
        1, 0,  # E (.)
        -1, -1, 1, 0,  # P (.--.)
        1, 1, 0,  # I (..)
        -1, 1, 1, 0,  # D (-..)
        1, -1, 0,  # A (.-)
        -1, 0,  # T (-)
        1, 1, 0,  # I (..)
        -1, -1, -1, 0,  # O (---)
        -1, 1, 0  # N (-.)
    ]

    current_time = 0
    interference_freq = 440  # Frequency that will emerge from interference

    # Add interference components
    for pattern in morse_pattern:
        if pattern in [-1, 1]:  # Both dots and dashes create sound
            duration = dash_duration if pattern == -1 else dot_duration
            samples = int(duration * sample_rate)
            t_segment = np.linspace(0, duration, samples)
            start_idx = int(current_time * sample_rate)
            end_idx = min(start_idx + samples, total_samples)
            segment_length = end_idx - start_idx

            # Create two components that will interfere
            # When combined: A + B = desired signal, A - B = noise
            interference1 = np.sin(2 * np.pi * interference_freq * t_segment[:segment_length])
            # interference2 = np.random.random(segment_length) * 2 - 1  # Random noise

            # Add to signals in a way that they'll interfere correctly
            signal1[start_idx:end_idx] += interference1
            # signal2[start_idx:end_idx] += (interference1 - interference2)

        current_time += duration + space_duration

    # Convert to 16-bit integer format
    signal1_int = np.int16(signal1 * 32767)
    signal2_int = np.int16(signal2 * 32767)

    # Save the files
    wavfile.write('audio1.wav', sample_rate, signal1_int)
    wavfile.write('audio2.wav', sample_rate, signal2_int)


# Generate the files
generate_audio_files()
