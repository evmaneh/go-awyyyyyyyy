import streamlit as st
from PIL import Image
import numpy as np

def make_transparent(image, threshold=128):
    img = Image.open(image).convert("RGBA")
    data = np.array(img)
    red, green, blue, alpha = data.T
    
    # Calculate luminance
    luminance = (0.2126 * red + 0.7152 * green + 0.0722 * blue).astype(np.uint8)
    
    # Calculate transparency based on luminance
    transparency = (255 - luminance)
    
    # Apply transparency threshold
    alpha = np.where(luminance < threshold, transparency, alpha)
    
    # Make the image transparent
    transparent_image = Image.fromarray(np.dstack((red, green, blue, alpha)))
    return transparent_image

def main():
    st.title("Image Transparency based on Luminance")
    st.write("Upload an image and adjust transparency based on luminance.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        threshold = st.slider("Transparency Threshold", 0, 255, 128)
        st.image(uploaded_image, caption="Original Image", use_column_width=True)

        transparent_image = make_transparent(uploaded_image, threshold)
        st.image(transparent_image, caption="Transparent Image", use_column_width=True)

if __name__ == "__main__":
    main()
