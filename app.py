import random
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="FabTech Python Game Arcade", page_icon="🎮", layout="wide"
)

# --- PASSWORD AUTHENTICATION SETUP ---
# Set your desired password here
APP_PASSWORD = "admin"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        "<h2 style='text-align: center;'>🔐 Streamlit Game Arcade Login</h2>",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            entered_password = st.text_input(
                "Enter Access Password", type="password"
            )
            submit_btn = st.form_submit_button("Login")
            if submit_btn:
                if entered_password == APP_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Incorrect password. Please try again.")
    st.stop()  # Halt execution until authenticated

# --- MAIN APP INTERFACE ---
st.title("🎮 Python & Streamlit Multi-Game Arcade")
st.write(
    "Welcome to your personal Streamlit game suite! Select a game from the tabs below."
)

# Create 5 Tabs for 5 Different Games
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🧩 2048 Lite", "🔤 Word Guess", "⏱️ High-Low Reflex", "🃏 Mini Blackjack", "🧠 Operations Trivia"]
)

# ==========================================
# TAB 1: 2048 Lite (Strategy & Logic)
# ==========================================
with tab1:
    st.header("🧩 2048 Puzzle (Grid Matrix)")
    st.write(
        "Combine matching numbers to reach higher values! Click buttons to shift numbers."
    )

    if "grid_2048" not in st.session_state:
        st.session_state.grid_2048 = [
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ]
        st.session_state.score_2048 = 0


    def display_grid(grid):
        for row in grid:
            cols = st.columns(4)
            for idx, val in enumerate(row):
                with cols[idx]:
                    if val == 0:
                        st.markdown(
                            "<div style='background-color:#eee; padding:20px; text-align:center; border-radius:5px; font-weight:bold; color:#aaa;'>-</div>",
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f"<div style='background-color:#ffcc00; padding:20px; text-align:center; border-radius:5px; font-weight:bold; color:#000;'>{val}</div>",
                            unsafe_allow_html=True,
                        )


    display_grid(st.session_state.grid_2048)
    st.write(f"**Score:** {st.session_state.score_2048}")

    col_l, col_r = st.columns(2)
    with col_l:
        if st.button("🔄 Reset 2048 Game"):
            st.session_state.grid_2048 = [
                [0, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0],
            ]
            st.session_state.score_2048 = 0
            st.rerun()
    with col_r:
        if st.button("🎲 Spawn Random Tile"):
            empty_cells = [
                (r, c)
                for r in range(4)
                for c in range(4)
                if st.session_state.grid_2048[r][c] == 0
            ]
            if empty_cells:
                r, c = random.choice(empty_cells)
                st.session_state.grid_2048[r][c] = random.choice([2, 4])
                st.session_state.score_2048 += 4
                st.rerun()


# ==========================================
# ==========================================
# TAB 2: Word Guess (Word / Vocabulary)
# ==========================================
with tab2:
    st.header("🔤 Word Guess Challenge")
    st.write("Guess the 5-letter secret word related to engineering or planning!")

    word_list = ["STEEL", "PLANT", "LEAN", "QUEUE", "AGILE", "CRANE"]

    if "secret_word" not in st.session_state:
        st.session_state.secret_word = random.choice(word_list)
        st.session_state.word_guesses = []

    guess_input = st.text_input(
        "Enter a 5-letter word:", max_chars=5, key="word_guess_input"
    )

    if st.button("Submit Guess"):
        if len(guess_input.upper()) != 5:
            st.warning("Please enter exactly 5 letters.")
        else:
            st.session_state.word_guesses.append(guess_input.upper())

    if st.session_state.word_guesses:
        st.write("### Past Guesses:")
        for g in st.session_state.word_guesses:
            feedback = ""
            for i, letter in enumerate(g):
                if i < len(st.session_state.secret_word):
                    if letter == st.session_state.secret_word[i]:
                        feedback += f"🟩 {letter} "
                    elif letter in st.session_state.secret_word:
                        feedback += f"🟨 {letter} "
                    else:
                        feedback += f"⬛ {letter} "
            st.write(f"**{g}** → {feedback}")

            if g == st.session_state.secret_word:
                st.success("🎉 Correct! You guessed the word!")

    if st.button("🔄 New Word"):
        st.session_state.secret_word = random.choice(word_list)
        st.session_state.word_guesses = []
        st.rerun()
# ==========================================
# ==========================================
# TAB 3: High-Low Reflex (Arcade / Numbers)
# ==========================================
with tab3:
    st.header("⏱️ Number High-Low Range Guess")
    st.write("I've picked a number between **1 and 100**. Try to guess it!")

    if "target_num" not in st.session_state:
        st.session_state.target_num = random.randint(1, 100)
        st.session_state.attempts = 0

    user_val = st.number_input(
        "Enter your guess:", min_value=1, max_value=100, step=1, key="hl_input"
    )

    if st.button("Check Guess"):
        st.session_state.attempts += 1
        if user_val < st.session_state.target_num:
            st.info("📉 Too Low! Aim higher.")
        elif user_val > st.session_state.target_num:
            st.info("📈 Too High! Aim lower.")
        else:
            st.success(
                f"🎯 Spot on! You found the number in {st.session_state.attempts} attempts."
            )

    if st.button("🔄 Reset High-Low"):
        st.session_state.target_num = random.randint(1, 100)
        st.session_state.attempts = 0
        st.rerun()

# ==========================================
# TAB 4: Mini Blackjack (Card / Probability)
# ==========================================
with tab4:
    st.header("🃏 Mini Blackjack (Card Game)")
    st.write("Get as close to 21 as possible without going over!")

    if "player_hand" not in st.session_state:
        st.session_state.player_hand = [
            random.randint(1, 11),
            random.randint(1, 11),
        ]
        st.session_state.dealer_card = random.randint(1, 11)
        st.session_state.bj_status = "Playing"


    def hand_sum(hand):
        return sum(hand)


    st.write(f"Dealer's Visible Card: **{st.session_state.dealer_card}**")
    st.write(f"Your Hand: **{st.session_state.player_hand}** (Total: {hand_sum(st.session_state.player_hand)})")

    if st.session_state.bj_status == "Playing":
        col_hit, col_stand = st.columns(2)
        with col_hit:
            if st.button("Hit"):
                st.session_state.player_hand.append(random.randint(1, 11))
                if hand_sum(st.session_state.player_hand) > 21:
                    st.session_state.bj_status = "Bust"
                st.rerun()
        with col_stand:
            if st.button("Stand"):
                dealer_total = st.session_state.dealer_card + random.randint(
                    1, 11
                )
                p_total = hand_sum(st.session_state.player_hand)
                if dealer_total > 21 or p_total > dealer_total:
                    st.session_state.bj_status = "Win"
                elif p_total == dealer_total:
                    st.session_state.bj_status = "Tie"
                else:
                    st.session_state.bj_status = "Lose"
                st.rerun()

    if st.session_state.bj_status == "Bust":
        st.error("💥 Bust! Total exceeded 21.")
    elif st.session_state.bj_status == "Win":
        st.success("🎉 You Win!")
    elif st.session_state.bj_status == "Lose":
        st.error("❌ Dealer Wins!")
    elif st.session_state.bj_status == "Tie":
        st.info("🤝 It's a Tie!")

    if st.button("🔄 Deal New Hand"):
        st.session_state.player_hand = [
            random.randint(1, 11),
            random.randint(1, 11),
        ]
        st.session_state.dealer_card = random.randint(1, 11)
        st.session_state.bj_status = "Playing"
        st.rerun()


# ==========================================
# TAB 5: Operations Trivia (Quiz Game)
# ==========================================
with tab5:
    st.header("🧠 Operations & Planning Trivia")
    st.write("Test your knowledge on manufacturing, supply chain, and project management principles.")

    questions = [
        {
            "q": "What does TOC stand for in manufacturing management?",
            "options": [
                "Theory of Constraints",
                "Total Order Control",
                "Time Optimized Cycle",
                "Transfer of Capital",
            ],
            "answer": "Theory of Constraints",
        },
        {
            "q": "Which chart is primarily used for project scheduling and tracking task dependencies?",
            "options": [
                "Pie Chart",
                "Gantt Chart",
                "Scatter Plot",
                "Pareto Chart",
            ],
            "answer": "Gantt Chart",
        },
        {
            "q": "What does TPI stand for during structural steel fabrication quality audits?",
            "options": [
                "Total Plant Inspection",
                "Third-Party Inspection",
                "Technical Process Indicator",
                "Time Performance Index",
            ],
            "answer": "Third-Party Inspection",
        },
    ]

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.trivia_score = 0

    if st.session_state.q_index < len(questions):
        current_q = questions[st.session_state.q_index]
        st.subheader(f"Question {st.session_state.q_index + 1} of {len(questions)}")
        st.write(current_q["q"])

        user_choice = st.radio(
            "Select an option:",
            current_q["options"],
            key=f"q_{st.session_state.q_index}",
        )

        if st.button("Submit Answer"):
            if user_choice == current_q["answer"]:
                st.success("Correct!")
                st.session_state.trivia_score += 1
            else:
                st.error(
                    f"Incorrect. The correct answer was: {current_q['answer']}"
                )
            st.session_state.q_index += 1
            st.rerun()
    else:
        st.write("### Quiz Completed! 🎉")
        st.write(
            f"Your Final Score: **{st.session_state.trivia_score} / {len(questions)}**"
        )
        if st.button("🔄 Restart Quiz"):
            st.session_state.q_index = 0
            st.session_state.trivia_score = 0
            st.rerun()

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Powered by Python & Streamlit | Secured Arcade</p>",
    unsafe_allow_html=True,
)
