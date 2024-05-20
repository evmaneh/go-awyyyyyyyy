import streamlit as st
import cv2
import numpy as np
from PIL import Image

def median_filter(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)

def main():
    st.title("Image Median Filter")
    st.write("Upload an image and apply a median filter with a kernel size of 5x5 pixels.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Convert the image to numpy array
        img_array = np.array(image)

        # Apply median filter
        filtered_img_array = median_filter(img_array, kernel_size=5)

        # Convert numpy array back to image
        filtered_image = Image.fromarray(filtered_img_array)

        # Display the filtered image
        st.image(filtered_image, caption="Filtered Image", use_column_width=True)

if __name__ == "__main__":
    main()
