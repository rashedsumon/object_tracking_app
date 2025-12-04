"""
app.py
Streamlit app for real-time 4-object tracking
"""

import streamlit as st
from tracker import track_objects
import os

st.title("Real-time 4-Object Tracking")

# Upload a video
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
if uploaded_file is not None:
    video_path = os.path.join("videos", uploaded_file.name)
    os.makedirs("videos", exist_ok=True)
    
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.video(video_path)
    
    if st.button("Start Tracking"):
        st.write("Tracking 4 objects...")
        track_objects(video_path)
