import librosa
import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import lfilter

def change_voice(audio_path, effect):
    y, sr = librosa.load(audio_path, sr=None)

    if effect == "Normal":
        return y

    elif effect == "Robot":
        # Rectify and modulate
        y_robot = np.abs(y)
        y_robot = np.sin(2 * np.pi * 30 * np.arange(len(y_robot)) / sr) * y_robot
        return y_robot

    elif effect == "Chipmunk":
        return librosa.effects.pitch_shift(y, sr, n_steps=8)

    elif effect == "Darth Vader":
        return librosa.effects.pitch_shift(y, sr, n_steps=-8)

    elif effect == "Echo":
        delay = int(0.3 * sr)
        echo_signal = np.zeros(len(y) + delay)
        echo_signal[:len(y)] = y
        echo_signal[delay:] += 0.5 * y
        return echo_signal

    else:
        return y
