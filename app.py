import streamlit as st
import random

st.set_page_config(page_title="மச்சான் கேம் Battle!", page_icon="⚔️", layout="centered")

st.markdown("""
<style>
    .main { background-color: #1E1E2E; color: white; }
    .stButton>button {
        width: 100%; background-color: #ff4b4b; color: white;
        font-size: 20px; font-weight: bold; border-radius: 10px; padding: 10px;
    }
    .vs-box { text-align: center; font-size: 40px; font-weight: bold; color: #FFD700; margin: 20px 0; }
    .score-board {
        background-color: #252538; padding: 15px; border-radius: 10px;
        text-align: center; font-size: 22px; font-weight: bold; border: 2px dashed #00cc66;
    }
</style>
""", unsafe_allow_html=True)

st.title("🪨 📄 ✂️ கேம் Battle!")

if "player_score" not in st.session_state: st.session_state.player_score = 0
if "comp_score" not in st.session_state: st.session_state.comp_score = 0
if "game_locked" not in st.session_state: st.session_state.game_locked = False

st.markdown(f"<div class='score-board'>🏆 நீங்க: {st.session_state.player_score} | 🤖 கம்ப்யூட்டர்: {st.session_state.comp_score}</div>", unsafe_allow_html=True)
st.write("---")

options = ["stone", "paper", "scissors"]
emojis = {"stone": "🪨 கல்", "paper": "📄 காகிதம்", "scissors": "✂️ கத்தரிக்கோல்"}

if st.session_state.game_locked:
        st.error("🚨 ஆட்டம் லாக் ஆகிடுச்சு மாப்ள! \n\n👉 Send 1Rs to give a special message! 🤫")
        
        # 🔗 UPI Deep Link
        upi_url = "upi://pay?pa=albertsugumar086-1@oksbi&pn=Albert%20Sugumar&am=1&cu=INR"
        
        # 🎯 ட்ரிபிள் கோட்ஸ் வச்சு அழகா மாத்தியாச்சு மாப்ள!
        st.markdown(f"""<a href="{upi_url}" target="_blank" style="text-decoration: none;"><div style="background-color: #25D366; color: white; padding: 12px; text-align: center; border-radius: 8px; font-weight: bold; font-size: 16px;">📲 GPay-ல 1Rs அனுப்ப இங்க கிளிக் பண்ணு மாப்ள!</div></a>""", unsafe_allow_html=True)
        
        st.write("---")
        
        # 💸 ஸ்பெஷல் மெசேஜ் பட்டன் - இது இப்போ கரெக்டா 'if'க்கு உள்ள தள்ளி இருக்கு!
        if st.button("💸 காசு அனுப்பிட்டேன் மாப்ள! ஸ்பெஷல் மெசேஜ் காட்டு!"):
            st.success("🎉 ஸ்பெஷல் மெசேஜ் அன்லாக் ஆகிடுச்சு மாப்ள!")
            st.info("🥺 உண்மை என்னன்னா...")
            st.warning("👉 முதல்ல அந்த பச்சை பட்டனை அமுக்கி காசு அனுப்பிட்டு வா மாப்ள, அப்பதான் மெசேஜ் அன்லாக் ஆகும்! 😉")
            
            st.session_state.game_locked = True
            st.button("🎮 பாசக்கார பயலே.. அடுத்த மேட்ச் விளையாடு மாப்ள!")
else:
    st.subheader("உங்க சாய்ஸ் என்ன மாப்ள?")
    col1, col2, col3 = st.columns(3)
    player_choice = None
    with col1:
        if st.button("🪨 STONE"): player_choice = "stone"
    with col2:
        if st.button("📄 PAPER"): player_choice = "paper"
    with col3:
        if st.button("✂️ SCISSORS"): player_choice = "scissors"

    if player_choice:
        comp_choice = random.choice(options)
        c1, c2, c3 = st.columns([2, 1, 2])
        with c1: st.subheader(f"👨‍💻 நீங்க:\n{emojis[player_choice]}")
        with c2: st.markdown("<div class='vs-box'>VS</div>", unsafe_allow_html=True)
        with c3: st.subheader(f"🤖 கம்ப்யூட்டர்:\n{emojis[comp_choice]}")

        if player_choice == comp_choice: st.warning("💥 *மேட்ச் டை ஆகிடுச்சு!*")
        elif (player_choice == "stone" and comp_choice == "scissors") or \
             (player_choice == "paper" and comp_choice == "stone") or \
             (player_choice == "scissors" and comp_choice == "paper"):
            st.success("🎉 *நீங்க ஜெயிச்சிட்டீங்க!*")
            st.session_state.player_score += 1
        else:
            st.error("😜 *கம்ப்யூட்டர் ஜெயிச்சிடுச்சு!*")
            st.session_state.comp_score += 1

        st.session_state.game_locked = True
        st.button("அடுத்த மேட்ச் விளையாட கிளிக் பண்ணு ➡️")
