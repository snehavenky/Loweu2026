import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Loweu for Adithya", page_icon="❤️")

# Custom CSS for a Valentine's vibe
st.markdown("""
    <style>
    .stApp { background-color: #fffafb; }
    h1 { color: #e91e63; }
    h3 { color: #ad1457; }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Valentine's Day, Adithya!")
st.subheader("A personalized gift from the whole crew.")

# --- MEMORY SECTION ---
st.write("### Our Journey")
col1, col2 = st.columns(2)
with col1:
    st.metric("Years Together", "8") 
with col2:
    st.metric("Cats Managed", "2 (Pilli & Meemee)")

# --- THE "OUR LOWEUS RATING" SECTION ---
st.divider()
st.header("📊 Our Loweus Rating")
st.write("Measuring the levels of extreme love from your favorite housemates:")

col1, col2, col3 = st.columns(3)

with col1:
    # Updated to a more reliable icon link
    st.image("https://cdn-icons-png.flaticon.com/512/616/616430.png", width=100) 
    st.subheader("Pilli")
    st.write("🐾 **Loweus: MAX**")
    st.caption("Rating: 11/10. Dad is the best pillow. Requests more salmon in exchange for extra Loweu.")

with col2:
    # Updated to a reliable black cat icon link
    st.image("https://cdn-icons-png.flaticon.com/512/10522/10522261.png", width=100)
    st.subheader("Meemee")
    st.write("🐾 **Loweus: HIGH**")
    st.caption("Rating: 9.8/10. Appreciates the calm head-scratches and quiet presence. You are one of the few humans she fully trusts.")

with col3:
    # Baby icon link
    st.image("https://cdn-icons-png.flaticon.com/512/11550/11550774.png", width=100)
    st.subheader("Manya")
    st.write("🍼 **Loweus: INFINITY**")
    st.caption("Rating: Off the charts! You're the best at peek-a-boo and the only one allowed to make her laugh that hard.")

# --- THE INTERACTIVE PART ---
st.divider()
st.write("### Why you're the best...")
st.write("Click the button below to see one of the many reasons I love you.")

reasons = [
    "The way you are such an amazing Appa to Manya.",
    "Our shared love for gaming (even with the chaotic after-game fights!).",
    "The fact that you handle Pilli and Meemee like a pro.",
    "Your patience in always looking out for our future.",
    "How we navigated parenthood together with such a strong bond.",
    "Simply because you're my favorite person to explore national parks with.",
    "The way you make even the smallest moments in Mountain View feel like a big adventure.",
    "Because you are my home, no matter where in the world we are."
]

if st.button("Generate a Reason for Loweu"):
    st.balloons()
    selected_reason = random.choice(reasons)
    st.success(f"✨ {selected_reason}")

# --- THE "GIFT" SURPRISE ---
st.divider()
with st.expander("Click here for your Valentine's Surprise"):
    st.write("### 🎫 One Voucher for a Stress-Free Date Night!")
    st.write("This voucher entitles you to one evening of gaming or a hike of your choice, with all vegetarian snacks provided!")
    st.info("Code: BEST-HUSBAND-2026")

st.caption("Built with extreme Loweu by Sneha")
