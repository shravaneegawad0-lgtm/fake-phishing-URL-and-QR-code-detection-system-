import streamlit as st
import cv2
import numpy as np
import re
import time

# ------------------- URL CHECKER -------------------
def check_url(url):
    suspicious = False
    if re.search(r'\d{5,}', url):  # long numbers in URL
        suspicious = True
    if "@" in url or "-" in url:   # @ or - signs
        suspicious = True
    if not url.startswith(("http://", "https://")):
        suspicious = True
    return "Phishing / Unsafe 🚨" if suspicious else "Safe ✅"


# ------------------- QR SCANNER -------------------
def start_qr_scanner():
    cap = cv2.VideoCapture(0)
    qr_detector = cv2.QRCodeDetector()
    stframe = st.empty()

    detected_text = None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect and decode QR
        data, bbox, _ = qr_detector.detectAndDecode(frame)
        if bbox is not None: 
            pts = np.int32(bbox).reshape(-1, 2)
            # Draw green rectangle around QR
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)
            if data:
                detected_text = data
                cv2.putText(frame, data, (pts[0][0], pts[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        stframe.image(frame, channels="BGR")
        time.sleep(0.03)

        if detected_text:
            cap.release()
            cv2.destroyAllWindows()
            stframe.empty()   # 🔥 clears webcam display
            return detected_text

    cap.release()
    cv2.destroyAllWindows()
    stframe.empty()   # 🔥 clears webcam display
    return None


# ------------------- STREAMLIT UI -------------------
st.set_page_config(page_title="Fake URL & QR Detection", layout="centered")

st.title(" 🔐Fake URL & QR Detection System")
st.markdown("### Detect **Phishing URLs** and **Fake QR Codes** easily")

# --- URL Checker ---
st.subheader("🔍 URL Checker")
url = st.text_input("Enter a URL to check:")
if st.button("Check URL"):
    if url:
        result = check_url(url)
        if "Safe" in result:
            st.success(f"✅ **{result}**")
        else:
            st.error(f"🚨 **{result}**")
    else:
        st.warning("Please enter a URL!")

st.markdown("---")

# --- QR Code Scanner ---
st.subheader("📷 QR Code Scanner")
if st.button("Start Scanning"):
    qr_text = start_qr_scanner()
    if qr_text:
        st.success(f"✅ QR Content: {qr_text}")
        result = check_url(qr_text)
        if "Safe" in result:
            st.success(f"✅ **{result}**")
        else:
            st.error(f"🚨 **{result}**")
    else:
        st.error("No QR code detected")
