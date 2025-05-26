import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("OCR Dokumen Bahasa Indonesia dengan EasyOCR")

uploaded_file = st.file_uploader("Upload gambar dokumen", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar yang di-upload", use_column_width=True)

    reader = easyocr.Reader(['id'])
    result = reader.readtext(np.array(image), detail=0)
    st.subheader("Hasil OCR:")
    st.write(" ".join(result))
