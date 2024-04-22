import streamlit as st
from PIL import Image
import tempfile
import subprocess
import os
import shutil

def detect_license(image_path, weights_path):
    output_dir = "./runs/detect/"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "detected.jpg")
    
    command = f"python C://Users//bhaga//Downloads//ML//automatic-number-plate-recognition//yolov9//detect.py --weights {weights_path} --source {image_path} --save-txt --save-conf"
    subprocess.run(command, shell=True)
    
    return output_file

def main():
    st.title("License Plate Detection")
    st.write("Upload an image or video to detect license plates.")
    
    uploaded_file = st.file_uploader("Choose an image or video...", type=["jpg", "jpeg", "png", "mp4"])
    
    if uploaded_file is not None:
        # Save uploaded file to a temporary directory
        temp_dir = "C:/Users/bhaga\Downloads/ML/automatic-number-plate-recognition/output"
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Display uploaded image or video
        st.image(temp_file_path, use_column_width=True)
        
        # Detect license plate
        weights_path = "C:\\Users\\bhaga\\Downloads\ML\\automatic-number-plate-recognition\yolov9\\license-detector.pt"
        output_file = detect_license(temp_file_path, weights_path)
        
        # Display detected image
        st.subheader("Detected License Plate")
        # if os.path.exists(output_file):
        detected_image = Image.open(output_file)
        st.image(detected_image, use_column_width=True)
        # else:
        #     st.write("No license plate detected.")
if __name__ == "__main__":
    main()