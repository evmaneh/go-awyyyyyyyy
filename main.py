import streamlit as st
import cv2
import numpy as np
from PIL import Image

def median_filter(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)

def find_edges(image):
    return cv2.Canny(image, 100, 200)

def overlay_images(background, overlay):
    overlay_mask = cv2.cvtColor(overlay, cv2.COLOR_GRAY2BGR)
    overlay_mask[np.all(overlay == [0, 0, 0], axis=-1)] = [255, 255, 255]
    return cv2.addWeighted(overlay_mask, 0.5, background, 0.5, 0)

def main():
    st.title("Image Median Filter with Find Edges Effect")
    st.write("Upload an image and apply a median filter with a kernel size of 5x5 pixels to the bottom layer, and apply the find edges effect to the top layer.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Convert the image to numpy array
        img_array = np.array(image)

        # Apply median filter to the bottom layer
        filtered_img_array = median_filter(img_array, kernel_size=5)

        # Duplicate the layer
        duplicate_layer = np.copy(filtered_img_array)

        # Apply find edges effect to the top layer
        edges_img_array = find_edges(duplicate_layer)

        # Overlay edges image onto the median filtered image
        overlayed_image = overlay_images(filtered_img_array, edges_img_array)

        # Convert numpy array back to image
        overlayed_image = Image.fromarray(overlayed_image)

        # Display the filtered image and edges image
        st.image(overlayed_image, caption="Overlayed Image", use_column_width=True)

if __name__ == "__main__":
    main()
