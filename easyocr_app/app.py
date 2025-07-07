import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import streamlit.components.v1 as components

ga_id = st.secrets["GA_ID"]

# Sisipkan Google Analytics Tracking Script
ga_code = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{{{dataLayer.push(arguments);}}}}
  gtag('js', new Date());
  gtag('config', '{ga_id}');
  gtag('event', 'page_view');
</script>
"""

components.html(ga_code, height=100, width=300)

st.title("OCR Dokumen Bahasa Indonesia dengan EasyOCR")

uploaded_file = st.file_uploader("Upload gambar dokumen", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar yang di-upload", use_container_width=True)

    reader = easyocr.Reader(['id'])
    result = reader.readtext(np.array(image), detail=0)

    st.subheader("Hasil OCR:")
    st.write(" ".join(result))
