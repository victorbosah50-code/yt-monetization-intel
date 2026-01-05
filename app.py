import streamlit as st
from scoring import calculate_score

st.set_page_config(page_title="YouTube Monetization Tool", layout="centered")

st.title("🎯 YouTube Monetization Intelligence Tool")
st.write("Enter your video title and length to see your monetization potential.")

title = st.text_input("Enter your video title:")
length = st.number_input("Enter video length (minutes):", min_value=1, max_value=60, value=10)

if st.button("Check Monetization"):
    score = calculate_score(title, length)
    st.metric("Monetization Score", score)

    if score >= 70:
        st.success("✅ Strong monetization potential")
    elif score >= 50:
        st.warning("⚠️ Average — consider improving title or length")
    else:
        st.error("❌ Low — revise before posting")
