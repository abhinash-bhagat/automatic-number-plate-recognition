import streamlit as st
from PIL import Image
import subprocess
import os
import glob

def detect_license(image_path, weights_path):
    # output_dir = "./output"
    # os.makedirs(output_dir, exist_ok=True)

    # Run detection
    command = f"python C://Users//bhaga//Downloads//ML//automatic-number-plate-recognition//yolov9//detect.py --conf 0.2 --weights {weights_path} --source {image_path} --save-txt --save-conf"
    subprocess.run(command, shell=True)

    # Find the latest directory created in runs/detect
    detect_dir = max(glob.glob("./yolov9/runs/detect/*"), key=os.path.getmtime)

    # Check if any image files are saved in the directory
    image_files = glob.glob(os.path.join(detect_dir, "*.jpg"))
    video_files = glob.glob(os.path.join(detect_dir, "*.mp4"))

    # Combine the lists
    all_files = image_files + video_files
    if all_files:
        detected_output = all_files[0]  # Get the first image file
        return detected_output, detect_dir
    else:
        return None, None  # Return None if no image files are found

# reader = easyocr.Reader(['en'], gpu=False)


# def perform_ocr_on_image(img, coordinates):
#     x, y, w, h = map(int, coordinates)
#     cropped_img = img[y:h, x:w]
#     gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2GRAY)
#     results = reader.readtext(gray_img)

#     text = ""
#     for res in results:
#         # Check if OCR result is not empty and confidence score is above threshold
#         if res[1] and len(res[1]) > 6 and res[2] > 0.2:
#             text = res[1]
#             break  # Stop iterating if valid text is found

#     return str(text)


def main():
    st.title("License Plate Detection")
    st.write("Upload an image or video to detect license plates.")
    
    uploaded_file = st.file_uploader("Choose an image or video...", type=["jpg", "jpeg", "png", "mp4"])
    
    if uploaded_file is not None:
        # Save uploaded file to a temporary directory
        temp_dir = "C:/Users/bhaga/Downloads/ML/automatic-number-plate-recognition/outputs/"
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Detect license plate
        weights_path = "C:\\Users\\bhaga\\Downloads\ML\\automatic-number-plate-recognition\yolov9\\license-detector.pt"
        output_file, detect_dir = detect_license(temp_file_path, weights_path)
        # Display original image
        st.subheader("Original Video")
        # original_image = Image.open(temp_file_path)
        # st.image(original_image, use_column_width=True)
        video_file = open(temp_file_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        # Display images side by side
        if output_file is not None:
            st.success('Output Successfully')
            # col1, col2 = st.columns(2)
            # with col1:
            #     # Display original image
            #     st.subheader("Original Video")
            #     # original_image = Image.open(temp_file_path)
            #     # st.image(original_image, use_column_width=True)
            #     video_file = open(temp_file_path, 'rb')
            #     video_bytes = video_file.read()
            #     st.video(video_bytes)
                
            # with col2:
            #     # Display detected image
            #     st.subheader("Detected License Plate")
            #     # detected_image = Image.open(output_file)
            #     # st.image(detected_image, use_column_width=True)
            #     output_video_file = open(output_file, 'rb')
            #     output_video_bytes = output_video_file.read()
            #     st.video(output_video_bytes)
        else:
            st.write("No license plate detected.")

if __name__ == "__main__":
    main()