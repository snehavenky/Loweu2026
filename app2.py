import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Loweu for Adithya", page_icon="❤️")

# Custom CSS for a Valentine's vibe
st.markdown("""
    <style>
    .main { background-color: #fffafb; }
    h1 { color: #e91e63; }
    .stMetric { background-color: #ffebee; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Valentine's Day, Adithya!")
st.subheader("A little something I built just for you.")

# --- MEMORY SECTION ---
st.write("### Our Journey")
col1, col2 = st.columns(2)
with col1:
    st.metric("Years Together", "8") 
with col2:
    st.metric("Cats Managed", "2 (Pilli & Meemee)")

# --- THE INTERACTIVE PART ---
st.divider()
st.write("### Why you're the best...")
st.write("Click the button below to see one of the many reasons I love you.")

reasons = [
    "The way you are such an amazing Appa to Manya.",
    "Our shared love for gaming and the chaotic after-game fights.",
    "The fact that you handle Pilli and Meemee like a pro.",
    "Your patience in always looking out for our future.",
    "How we navigated the first year of parenthood together.",
    "Simply because you're my favorite person to explore National Parks with.",
    "The way you always find the best vegetarian spots for our date nights.",
    "Being my partner-in-crime for every K-drama marathon.",
    "How you support my AI/ML rabbit holes and 'A-Sync' brainstorms.",
    "The way you make our home in Mountain View feel like the best place on earth.",
    "Your 'Loweu' is the highlight of my every single day."
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

# --- THE "OUR LOWEUS RATING" SECTION ---
st.divider()
st.header("📊 Our Loweus Rating")
st.write("Measuring the levels of extreme love from your favorite housemates:")

col1, col2, col3 = st.columns(3)

with col1:
    # Reliable Orange Cat Emoji
    st.image("https://openmoji.org/data/color/svg/1F408-200D-1F080.svg", width=100) 
    st.subheader("Pilli")
    st.write("🐾 **Loweus: MAX**")
    st.caption("Rating: 11/10. Dad is the best pillow. Requests more salmon in exchange for extra Loweu.")

with col2:
    # Reliable Black Cat Emoji
    st.image("https://openmoji.org/data/color/svg/1F408-200D-1F311.svg", width=100)
    st.subheader("Meemee")
    st.write("🐾 **Loweus: Infinite**")
    st.caption("Rating: 10/10. Even though I'm sleek and independent, I'll always scream for Dad's attention first.")

with col3:
    # Baby Emoji for Manya
    st.image("https://openmoji.org/data/color/svg/1F476.svg", width=100)
    st.subheader("Manya")
    st.write("🍼 **Loweus: Beyond Measure**")
    st.caption("Rating: 100/10. Best Appa ever. Loves your silly faces and the way you always keep me safe.")

st.divider()
st.caption("Built with ❤️ by Sneha")
