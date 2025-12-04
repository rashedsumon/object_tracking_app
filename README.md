# Real-Time 4-Object Tracking App

## Overview
This project tracks 4 identical-looking objects in real-time using YOLO + DeepSORT tracker, maintaining consistent IDs across frames. The app is deployed with Streamlit.

## Folder Structure
- `app.py` : Main Streamlit app
- `data_loader.py` : Downloads dataset from KaggleHub
- `tracker.py` : Object tracking logic
- `videos/` : Input videos uploaded by the user
- `models/` : YOLO model weights

## Setup
1. Clone the repo.
2. Install Python 3.11.0.
3. Install dependencies:
