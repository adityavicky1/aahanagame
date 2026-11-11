import random
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Toddler Fun Arcade", page_icon="🎈", layout="wide"
)

# --- PASSWORD AUTHENTICATION SETUP ---
APP_PASSWORD = "admin"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        "<h2 style='text-align: center;'>🔐 Parent Login to Toddler Arcade</h2>",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            entered_password = st.text_input(
                "Enter Password (default: admin)", type="password"
            )
            submit_btn = st.form_submit_button("Enter Arcade")
            if submit_btn:
                if entered_password == APP_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Incorrect password. Try again.")
    st.stop()  # Stop execution until authenticated

# --- MAIN TODDLER APP ---
st.title("🌟 Aahana's Toddler Play Zone 🌟")
st.write(
    "Welcome! Choose a game below designed especially for little fingers and big imaginations."
)

# Create 3 Tabs for the 3 Toddler Games
tab1, tab2, tab3 = st.tabs(
    ["🎈 Balloon Pop", "🎨 Color & Shape Match", "🦁 Animal Sound Box"]
)

# ==========================================
# TAB 1: BALLOON POP
# ==========================================
with tab1:
    st.header("🎈 Pop the Balloons!")
    st.write("Tap the buttons below to pop the balloons!")

    if "balloons_popped" not in st.session_state:
        st.session_state.balloons_popped = 0

    balloon_cols = st.columns(5)
    colors = ["🔴", "🔵", "🟢", "🟡", "🟣"]
    names = ["Red", "Blue", "Green", "Yellow", "Purple"]

    for i in range(5):
        with balloon_cols[i]:
            if st.button(f"{colors[i]}\nPop!", key=f"balloon_{i}"):
                st.balloons()
                st.session_state.balloons_popped += 1
                st.success(f"Pop! You popped the {names[i]} balloon!")

    st.write(
        f"### 🎉 Total Balloons Popped: {st.session_state.balloons_popped}"
    )

    if st.button("🔄 Reset Balloons"):
        st.session_state.balloons_popped = 0
        st.rerun()

# ==========================================
# TAB 2: COLOR & SHAPE MATCH
# ==========================================
with tab2:
    st.header("🎨 Match the Colors")
    st.write("Can you find the matching color box?")

    if "target_color" not in st.session_state:
        st.session_state.target_color = random.choice(
            ["Red", "Blue", "Green", "Yellow"]
        )
        st.session_state.match_score = 0

    target = st.session_state.target_color
    st.markdown(
        f"<h3 style='text-align: center; color: #333;'>Find and click the: <span style='color: blue;'>{target}</span> box!</h3>",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    colors_dict = {
        "Red": "🔴",
        "Blue": "🔵",
        "Green": "🟢",
        "Yellow": "🟡",
    }

    with c1:
        if st.button("🔴 Red", key="btn_red"):
            chosen = "Red"
            if chosen == target:
                st.success("🌟 Yay! Correct!")
                st.session_state.match_score += 1
                st.session_state.target_color = random.choice(list(colors_dict.keys()))
                st.rerun()
            else:
                st.error("Oops! Try again.")

    with c2:
        if st.button("🔵 Blue", key="btn_blue"):
            chosen = "Blue"
            if chosen == target:
                st.success("🌟 Yay! Correct!")
                st.session_state.match_score += 1
                st.session_state.target_color = random.choice(list(colors_dict.keys()))
                st.rerun()
            else:
                st.error("Oops! Try again.")

    with c3:
        if st.button("🟢 Green", key="btn_green"):
            chosen = "Green"
            if chosen == target:
                st.success("🌟 Yay! Correct!")
                st.session_state.match_score += 1
                st.session_state.target_color = random.choice(list(colors_dict.keys()))
                st.rerun()
            else:
                st.error("Oops! Try again.")

    with c4:
        if st.button("🟡 Yellow", key="btn_yellow"):
            chosen = "Yellow"
            if chosen == target:
                st.success("🌟 Yay! Correct!")
                st.session_state.match_score += 1
                st.session_state.target_color = random.choice(list(colors_dict.keys()))
                st.rerun()
            else:
                st.error("Oops! Try again.")

    st.write(f"**Score:** {st.session_state.match_score} 🏆")

# ==========================================
# TAB 3: ANIMAL SOUND EXPLORER
# ==========================================
with tab3:
    st.header("🦁 Animal Sound Box")
    st.write("Click an animal to see what it says!")

    animal_cols = st.columns(4)
    animals = [
        {"name": "Lion", "emoji": "🦁", "sound": "Roar! 🦖"},
        {"name": "Cow", "emoji": "🐮", "sound": "Moo! 🥛"},
        {"name": "Duck", "emoji": "🦆", "sound": "Quack Quack! 🌊"},
        {"name": "Dog", "emoji": "🐶", "sound": "Woof Woof! 🦴"},
    ]

    for idx, animal in enumerate(animals):
        with animal_cols[idx]:
            if st.button(f"{animal['emoji']}\n{animal['name']}", key=f"animal_{idx}"):
                st.markdown(
                    f"<h2 style='text-align: center;'>{animal['emoji']} The {animal['name']} says: <b>{animal['sound']}</b></h2>",
                    unsafe_allow_html=True,
                )
                st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ for Toddler Fun via Streamlit</p>",
    unsafe_allow_html=True,
)
