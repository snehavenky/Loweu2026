import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Loweu for Adithya", page_icon="❤️")

# Custom CSS for a Valentine's vibe
st.markdown("""
    <style>
    .main { background-color: #fffafb; }
    h1 { color: #e91e63; }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Valentine's Day, Adithya!")
st.subheader("A little something I built just for you.")

# --- MEMORY SECTION ---
st.write("### Our Journey")
col1, col2 = st.columns(2)
with col1:
    st.metric("Years Together", "8") # Fill in your years!
with col2:
    st.metric("Cats Managed", "2 (Pilli & Meemee)")

# --- THE INTERACTIVE PART ---
st.divider()
st.write("### Why you're the best...")
st.write("Click the button below to see one of the many reasons I love you.")

reasons = [
    "The way you are such an amazing Appa to Manya.",
    "Our shared love for gaming and the chaotic after game fights",
    "The fact that you handle Pilli and Meemee like a pro.",
    "Your patience in always looking out for our future",
    "How we navigated parenthood together."
    "Simply because you're my favorite person to explore national parks with."
]

if st.button("Generate a Reason"):
    st.balloons()
    selected_reason = random.choice(reasons)
    st.success(f"✨ {selected_reason}")

# --- THE "GIFT" SURPRISE ---
st.divider()
with st.expander("Click here for your Valentine's Surprise"):
    st.write("### 🎫 One Voucher for a Stress-Free Date Night!")
    st.write("This voucher entitles you to one evening of gaming or a hike of your choice, with all vegetarian snacks provided!")
    st.info("Code: BEST-HUSBAND-2026")

st.caption("Built with ❤️ by Sneha")
st.subheader("A personalized gift from the whole crew.")

# --- THE "OUR LOWEUS RATING" SECTION ---
st.divider()
st.header("📊 Our Loweus Rating")
st.write("Measuring the levels of extreme love from your favorite housemates:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://img.icons8.com/color/96/orange-cat.png") # Pilli
    st.subheader("Pilli")
    st.write("🐾 **Loweus: MAX**")
    st.caption("Rating: 11/10. Dad is the best pillow. Requests more salmon in exchange for extra Loweu.")

with col2:
    st.image("https://img.icons8.com/color/96/black-cat.png")
    st.subheader("Meemee")
    
