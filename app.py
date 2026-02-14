import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Loweu for Adithya", page_icon="❤️")

# Custom CSS for a Valentine's vibe and transparent pink metrics
st.markdown("""
    <style>
    .main { background-color: #fffafb; }
    h1 { color: #e91e63; }
    
    /* Transparent pink hue for metrics */
    [data-testid="stMetric"] {
        background-color: rgba(255, 182, 193, 0.2); 
        border: 1px solid rgba(233, 30, 99, 0.3);
        padding: 15px;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("❤️ Happy Valentine's Day!")
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
    "How we navigated parenthood together.",
    "Simply because you're my favorite person to explore national parks with.",
    "How you somehow always know which vegetarian snack I'm craving.",
    "The way you support my AI/ML ideas, even the wild ones.",
    "Because you make every day in Mountain View feel like an adventure.",
    "Your 'Loweu' is truly one of a kind."
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
    # Orange Cat (Noto Emoji)
    st.image("https://fonts.gstatic.com/s/e/notoemoji/latest/1f408/512.png", width=100) 
    st.subheader("Pilli")
    st.write("🐾 **Loweus: Conditional**")
    st.caption("Rating: 7/10. You are technically the secondary human, but his Loweu spikes significantly whenever you're the one opening the wet food.")

with col2:
    # Black Cat (Noto Emoji)
    st.image("https://img.icons8.com/color/144/black-cat.png", width=100)
    st.subheader("Meemee")
    st.write("🐾 **Loweus: Cozy**")
    st.caption("Rating: 12/10. Claims your legs as her permanent snuggle territory. No movement allowed.")

with col3:
    # Baby Girl (Noto Emoji)
    st.image("https://fonts.gstatic.com/s/e/notoemoji/latest/1f467/512.png", width=100)
    st.subheader("Manya")
    st.write("🍼 **Loweus: Peak**")
    st.caption("Rating: Infinite. Especially loves your various different 'Hi-Fi's' and thinks you're the coolest Appa.")

st.divider()
st.caption("Built with ❤️ by Sneha")
