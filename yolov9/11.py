import streamlit as st
import os

uploaded_file = st.file_uploader("Choose an image or video...", type=["jpg", "jpeg", "png", "mp4"])
temp_dir = "C:/Users/bhaga/Downloads/ML/automatic-number-plate-recognition/outputs/"
temp_file_path = os.path.join(temp_dir, uploaded_file.name)


col1, col2 = st.columns(2)
with col1:
    # Display original image
    st.subheader("Original Video")
    # original_image = Image.open(temp_file_path)
    # st.image(original_image, use_column_width=True)
    video_file = open(temp_file_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
                
with col2:
    # Display detected image
    st.subheader("Detected License Plate")
    # detected_image = Image.open(output_file)
    # st.image(detected_image, use_column_width=True)
    output_video_file = open(temp_file_path, 'rb')
    output_video_bytes = output_video_file.read()
    st.video(output_video_bytes)