import streamlit as st
import cv2
from yolo_people_counter import PeopleCounter
from PIL import Image
import tempfile

st.title("🧍 Real-Time People Counting with YOLO")
st.markdown("Upload video or use webcam to count people in real-time.")

counter = PeopleCounter("Kelompok2Model.pt")

source_type = st.selectbox("Select source", ["📹 Upload Video", "📷 Webcam (Local Only)"])

frame_window = st.image([])
count_text = st.markdown("Total People Detected: 0")

if source_type == "📹 Upload Video":
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mpeg4"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture(tfile.name)

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
        cap.release()
    else:
        st.warning("Please upload a video file.")

elif source_type == "📷 Webcam (Local Only)":
    run = st.checkbox("Start Webcam (Local Only)")

    if run:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Webcam could not be opened.")
        else:
            while True:
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to capture frame from webcam.")
                    break
                frame = cv2.resize(frame, (640, 480))
                annotated, count = counter.process_frame(frame)
                frame_window.image(annotated, channels="BGR")
                count_text.markdown(f"**Total People Detected: {count}**")
            cap.release()
