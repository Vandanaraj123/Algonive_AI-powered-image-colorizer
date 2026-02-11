import streamlit as st
import cv2
import numpy as np
from colorizer import colorize_image
import tempfile

st.title("AI Image Colorizer 🎨")
st.write("Upload a black & white image to colorize it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.subheader("Original Image")
    st.image(image, channels="BGR")

    with st.spinner("Colorizing..."):
        colorized = colorize_image(image)

    st.subheader("Colorized Image")
    st.image(colorized, channels="BGR")

    # Save temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    cv2.imwrite(temp_file.name, colorized)

    with open(temp_file.name, "rb") as file:
        st.download_button(
            label="Download Colorized Image",
            data=file,
            file_name="colorized_output.jpg",
            mime="image/jpeg"
        )

