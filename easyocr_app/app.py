import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import streamlit.components.v1 as components
import sys
import contextlib
import os
import io

gtm_id = st.secrets["GTM_ID"]
gtm_code = f"""
<!-- Google Tag Manager -->
<script>
(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;
f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{gtm_id}');
</script>

<!-- Google Tag Manager (noscript) -->
<iframe src="https://www.googletagmanager.com/ns.html?id={gtm_id}"
height="0" width="0" style="display:none;visibility:hidden"></iframe>
"""
components.html(gtm_code, height=100, width=300)

st.title("OCR Dokumen Bahasa Indonesia dengan EasyOCR")

uploaded_file = st.file_uploader("Upload gambar dokumen", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar yang di-upload", use_container_width=True)

    with st.spinner("🔍 Memproses gambar, mohon tunggu..."):
        # Redirect stdout & stderr supaya user nggak lihat log PyTorch/EasyOCR
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            reader = easyocr.Reader(['id'], verbose=False)
            result = reader.readtext(np.array(image), detail=0)

    st.subheader("Hasil OCR:")
    st.write(" ".join(result))
