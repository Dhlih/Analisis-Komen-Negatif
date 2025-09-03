import streamlit as st
import joblib
import re

loaded_model = joblib.load("model1.pkl")
loaded_vectorizer = joblib.load("vectorizer.pkl")

st.title("Halo Selamat Datang")

comment = st.text_area("Masukkan komen")

if comment:
    clean_comment = re.sub(r"[^a-z\s]", " ", str(comment).lower())
    
    X_new = loaded_vectorizer.transform([clean_comment])
    
    result = loaded_model.predict_proba(X_new)[0]
    
    class_names = ["pornografi", "sara", "radikalisme", "pencemaran Nama Baik"]
    
    outputs = []
    for index, cls in enumerate(result):
        if cls >= 0.3:
            outputs.append(f"Komen Anda terdeteksi {class_names[index]} dengan keyakinan {cls:.2f}")
    
    if not outputs:
        outputs.append("Kami tidak yakin")
    
    for out in outputs:
        st.text(out)
