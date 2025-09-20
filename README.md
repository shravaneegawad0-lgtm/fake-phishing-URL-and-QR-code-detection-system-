# 🔐 Fake URL & QR Code Detection System  

This project is a web-based security tool  built using ython, OpenCV, and Streamlit to help detect phishing URLs and malicious QR codes in real time.  


## 📌 Features  
- ✅ URL Checker 
  - Detects suspicious URLs based on phishing patterns (long numeric strings, use of `@` or `-`, missing `http/https`).  
    Shows results clearly with Safe ✅ or Phishing 🚨 indicators.  

 📷 QR Code Scanner (Webcam-based)
  - Uses your webcam to scan QR codes in real time.  
  - Highlights QR codes with a green rectangle when detected.  
  - Automatically checks whether the QR content (URL/text) is safe or phishing.  
  - Webcam closes automatically after successful scan.  


## 🛠️ Tech Stack  
- Python 3 
- Streamlit – Web UI framework  
- OpenCV – For webcam and QR code detection  
- Regex (re)– For phishing URL detection  

## 🚀 Installation & Run  
1. Install dependencies:
  - pip install streamlit opencv-python
    
2. Run the app:
  -python -m streamlit run qqq.py
