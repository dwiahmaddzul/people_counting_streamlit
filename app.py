import streamlit as st
import cv2
from yolo_people_counter import PeopleCounter
from PIL import Image
import tempfile

st.title("🧍 Real-Time People Counting with YOLO")
st.markdown("Upload video or use webcam to count people in real-time.")

counter = PeopleCounter("Kelompok2Model.pt")

source_type = st.selectbox("Select source", ["📷 Webcam", "📹 Upload Video"])

if source_type == "📹 Upload Video":
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture(tfile.name)

elif source_type == "📷 Webcam":
    cap = cv2.VideoCapture(0)

frame_window = st.image([])
count_text = st.markdown("Total People Detected: 0")

run = st.checkbox("Start People Counting")

if run and cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640, 480))
        annotated, count = counter.process_frame(frame)
        frame_window.image(annotated, channels="BGR")
        count_text.markdown(f"**Total People Detected: {count}**")
else:
    st.warning("Waiting for video input...")
=======
import streamlit as st
import cv2
from yolo_people_counter import PeopleCounter
from PIL import Image
import tempfile

st.title("🧍 Real-Time People Counting with YOLO")
st.markdown("Upload video or use webcam to count people in real-time.")

counter = PeopleCounter("best.pt")

source_type = st.selectbox("Select source", ["📷 Webcam", "📹 Upload Video"])

if source_type == "📹 Upload Video":
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture(tfile.name)

elif source_type == "📷 Webcam":
    cap = cv2.VideoCapture(0)

frame_window = st.image([])
count_text = st.markdown("Total People Detected: 0")

run = st.checkbox("Start People Counting")

if run and cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640, 480))
        annotated, count = counter.process_frame(frame)
        frame_window.image(annotated, channels="BGR")
        count_text.markdown(f"**Total People Detected: {count}**")
else:
    st.warning("Waiting for video input...")
