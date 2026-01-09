import streamlit as st
from scanner import scan_website, detect_trackers, calculate_risk

st.title("Reverse OSINT – Tracker Detection Tool")

url = st.text_input("Enter Website URL (include https://)")

if st.button("Scan Website"):
    if url:
        scripts = scan_website(url)
        trackers = detect_trackers(scripts)

        st.subheader("Detected Trackers")

        if trackers:
            for t in trackers:
                st.write(f"🔴 {t[0]} → {t[1]}")
        else:
            st.success("No trackers detected")

        risk = calculate_risk(len(trackers))
        st.subheader("Privacy Risk Level")
        st.write(risk)
    else:
        st.warning("Please enter a valid URL")
