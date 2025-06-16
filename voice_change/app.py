import streamlit as st
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav
from utils import change_voice

st.set_page_config(page_title="🎤 Real-Time Voice Changer")

st.title("🎙️ Real-Time Voice Changer")
st.markdown("Record your voice and apply cool effects!")

# --- Select voice effect ---
effect = st.selectbox("Choose Voice Effect", ["Normal", "Robot", "Chipmunk", "Darth Vader", "Echo"])

# --- Record audio ---
duration = st.slider("Recording Duration (seconds)", 1, 10, 3)
sample_rate = 44100

if st.button("🔴 Record"):
    st.info("Recording... Speak now!")
    recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    st.success("Recording Complete!")

    # --- Convert and save temp WAV ---
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_input.name, sample_rate, recording)

    # --- Apply effect ---
    modified_audio = change_voice(temp_input.name, effect)

    # --- Save output ---
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_output.name, sample_rate, modified_audio)

    # --- Playback & Download ---
    st.audio(temp_output.name, format='audio/wav')
    st.download_button("⬇️ Download Modified Audio", data=open(temp_output.name, 'rb'), file_name="modified.wav")
