import random
import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Aahana's Play Zone & Scratch Studio",
    page_icon="🌟",
    layout="wide"
)

# --- PASSWORD AUTHENTICATION SETUP ---
APP_PASSWORD = "admin"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        "<h2 style='text-align: center;'>🔐 Parent Login to Aahana's Play Zone</h2>",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            entered_password = st.text_input(
                "Enter Password (default: admin)", type="password"
            )
            submit_btn = st.form_submit_button("Enter Play Zone", use_container_width=True)
            if submit_btn:
                if entered_password == APP_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Incorrect password. Try again.")
    st.stop()  # Stop execution until authenticated

# --- MAIN TODDLER APP ---
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🌟 Aahana's Interactive Play Zone 🌟</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #555;'>Build animations with Scratch blocks or play fun games below!</h4>",
    unsafe_allow_html=True,
)

# Create 5 Interactive Tabs including the new Scratch-like Coding Studio
tab_scratch, tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🧩 Scratch Coding Studio",
        "🎈 Magic Balloon Pop",
        "🍎 Fruit Counting",
        "🦁 Animal Sound Box",
        "🎨 Color Matcher",
    ]
)

# ==========================================
# TAB 0: SCRATCH-STYLE INTERACTIVE BLOCK STUDIO
# ==========================================
with tab_scratch:
    st.header("🧩 Aahana's Scratch Coding Stage")
    st.write("Tap the colorful coding blocks to build a sequence, then press the **Green Flag 🚩** to watch your character dance, jump, spin, and play music!")

    # Embed a rich, self-contained HTML5/JS Scratch-like interactive canvas & block builder
    scratch_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
        <style>
            @keyframes bounceSprite {
                0%, 100% { transform: translateY(0) scale(1); }
                50% { transform: translateY(-70px) scale(1.15); }
            }
            @keyframes spinSprite {
                0% { transform: rotate(0deg) scale(1); }
                50% { transform: rotate(180deg) scale(1.2); }
                100% { transform: rotate(360deg) scale(1); }
            }
            @keyframes wiggleSprite {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(-20deg); }
                75% { transform: rotate(20deg); }
            }
            .anim-jump { animation: bounceSprite 0.6s ease-in-out; }
            .anim-spin { animation: spinSprite 0.7s ease-in-out; }
            .anim-dance { animation: wiggleSprite 0.5s ease-in-out 2; }
            .scratch-block {
                border-radius: 12px;
                box-shadow: 0 4px 0 rgba(0,0,0,0.2);
                transition: transform 0.1s;
                cursor: pointer;
                user-select: none;
            }
            .scratch-block:active {
                transform: translateY(3px);
                box-shadow: 0 1px 0 rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body class="bg-slate-50 p-3 font-sans">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
            
            <!-- Left: Block Palette -->
            <div class="lg:col-span-4 bg-white p-4 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wider mb-3">1. Tap Blocks to Add</h3>
                <div class="space-y-2.5">
                    <div onclick="addBlock('moveRight', '➡️ Move Right', 'bg-blue-500')" class="scratch-block bg-blue-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>➡️ Move Right</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('moveLeft', '⬅️ Move Left', 'bg-blue-600')" class="scratch-block bg-blue-600 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>⬅️ Move Left</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('jump', '⬆️ Jump High!', 'bg-purple-500')" class="scratch-block bg-purple-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>⬆️ Jump High!</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('spin', '🔄 Spin Around', 'bg-indigo-500')" class="scratch-block bg-indigo-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>🔄 Spin Around</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('sayHello', '💬 Say Hello!', 'bg-amber-500')" class="scratch-block bg-amber-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>💬 Say "Yay Aahana!"</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('playMusic', '🎵 Play Magic Note', 'bg-pink-500')" class="scratch-block bg-pink-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>🎵 Play Magic Music</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                    <div onclick="addBlock('changeBg', '🌈 Change Sky Color', 'bg-emerald-500')" class="scratch-block bg-emerald-500 text-white font-bold px-4 py-3 text-sm flex items-center justify-between">
                        <span>🌈 Change Background</span><span class="text-xs bg-white/20 px-2 py-0.5 rounded">+ Add</span>
                    </div>
                </div>

                <!-- Sprite Selector -->
                <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wider mt-5 mb-2">Pick Your Character</h3>
                <div class="grid grid-cols-4 gap-2">
                    <button onclick="setSprite('🐱')" class="text-2xl bg-slate-100 hover:bg-amber-100 p-2 rounded-xl border border-slate-200 transition">🐱</button>
                    <button onclick="setSprite('🦄')" class="text-2xl bg-slate-100 hover:bg-amber-100 p-2 rounded-xl border border-slate-200 transition">🦄</button>
                    <button onclick="setSprite('🦖')" class="text-2xl bg-slate-100 hover:bg-amber-100 p-2 rounded-xl border border-slate-200 transition">🦖</button>
                    <button onclick="setSprite('🚀')" class="text-2xl bg-slate-100 hover:bg-amber-100 p-2 rounded-xl border border-slate-200 transition">🚀</button>
                </div>
            </div>

            <!-- Middle: Script Workspace -->
            <div class="lg:col-span-3 bg-slate-100 p-4 rounded-2xl border-2 border-dashed border-slate-300 flex flex-col">
                <div class="flex justify-between items-center mb-3">
                    <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wider">2. Your Code Stack</h3>
                    <button onclick="clearBlocks()" class="text-xs bg-rose-100 text-rose-600 hover:bg-rose-200 font-bold px-2.5 py-1 rounded-lg transition">Clear All</button>
                </div>
                
                <div class="bg-amber-400 text-slate-900 font-extrabold px-4 py-2.5 rounded-t-2xl rounded-b-lg shadow-sm text-sm flex items-center gap-2 mb-2">
                    <span>🚩</span> When Green Flag Clicked
                </div>

                <div id="codeQueue" class="flex-grow space-y-1.5 min-h-[220px] max-h-[340px] overflow-y-auto pr-1">
                    <!-- Dynamic blocks render here -->
                </div>
            </div>

            <!-- Right: Interactive Stage -->
            <div class="lg:col-span-5 bg-white p-4 rounded-2xl shadow-sm border border-slate-200 flex flex-col">
                <div class="flex justify-between items-center mb-3">
                    <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wider">3. Play Stage</h3>
                    <div class="flex gap-2">
                        <button onclick="runCode()" id="runBtn" class="bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold px-4 py-2 rounded-xl shadow-md flex items-center gap-1.5 text-sm transition transform active:scale-95">
                            <span>🚩</span> GO!
                        </button>
                        <button onclick="resetStage()" class="bg-rose-500 hover:bg-rose-600 text-white font-bold px-3 py-2 rounded-xl shadow-md text-sm transition">
                            🛑 Reset
                        </button>
                    </div>
                </div>

                <!-- Stage Canvas -->
                <div id="stageArea" class="relative flex-grow min-h-[300px] rounded-2xl bg-gradient-to-b from-sky-200 to-emerald-100 border-2 border-slate-200 overflow-hidden flex items-center justify-center transition-colors duration-500">
                    <!-- Decorative Clouds & Sun -->
                    <div class="absolute top-4 right-5 text-4xl select-none">☀️</div>
                    <div class="absolute top-6 left-6 text-3xl opacity-80 select-none">☁️</div>
                    <div class="absolute bottom-0 w-full h-12 bg-emerald-400/50 border-t border-emerald-500/30"></div>

                    <!-- Speech Bubble -->
                    <div id="speechBubble" class="hidden absolute top-14 bg-white border-2 border-slate-800 text-slate-900 font-extrabold px-4 py-2 rounded-2xl shadow-lg text-base z-20 animate-bounce">
                        Yay Aahana! 🌟
                    </div>

                    <!-- Interactive Character Sprite -->
                    <div id="spriteContainer" style="transform: translateX(0px);" class="transition-transform duration-300 z-10 cursor-pointer" onclick="quickPoke()">
                        <div id="spriteEmoji" class="text-7xl select-none filter drop-shadow-md">🐱</div>
                    </div>
                </div>
                <p class="text-center text-xs text-slate-400 mt-2">Tip: Tap the character directly on stage for a surprise!</p>
            </div>
        </div>

        <script>
            let blocks = [
                { type: 'jump', label: '⬆️ Jump High!', color: 'bg-purple-500' },
                { type: 'playMusic', label: '🎵 Play Magic Music', color: 'bg-pink-500' },
                { type: 'sayHello', label: '💬 Say "Yay Aahana!"', color: 'bg-amber-500' }
            ];
            let posX = 0;
            let isRunning = false;
            const bgThemes = [
                'from-sky-200 to-emerald-100',
                'from-purple-200 to-pink-100',
                'from-amber-200 to-orange-100',
                'from-indigo-900 to-purple-800'
            ];
            let bgIndex = 0;

            function playTone(note = "C5") {
                try {
                    const synth = new Tone.Synth().toDestination();
                    synth.triggerAttackRelease(note, "8n");
                } catch (e) {}
            }

            function renderBlocks() {
                const container = document.getElementById('codeQueue');
                container.innerHTML = '';
                if (blocks.length === 0) {
                    container.innerHTML = '<div class="text-center text-slate-400 text-xs py-10">Tap blocks on the left to build your program!</div>';
                    return;
                }
                blocks.forEach((b, idx) => {
                    const div = document.createElement('div');
                    div.id = `block-step-${idx}`;
                    div.className = `${b.color} text-white font-bold px-3.5 py-2.5 rounded-xl text-xs flex justify-between items-center shadow-sm transition-all`;
                    div.innerHTML = `
                        <span>${idx + 1}. ${b.label}</span>
                        <button onclick="removeBlock(${idx})" class="bg-black/20 hover:bg-black/40 rounded-full w-5 h-5 flex items-center justify-center text-[10px]">✕</button>
                    `;
                    container.appendChild(div);
                });
            }

            function addBlock(type, label, color) {
                playTone("E5");
                blocks.push({ type, label, color });
                renderBlocks();
            }

            function removeBlock(idx) {
                blocks.splice(idx, 1);
                renderBlocks();
            }

            function clearBlocks() {
                blocks = [];
                renderBlocks();
            }

            function setSprite(emoji) {
                playTone("G5");
                document.getElementById('spriteEmoji').innerText = emoji;
            }

            function resetStage() {
                posX = 0;
                const container = document.getElementById('spriteContainer');
                container.style.transform = `translateX(0px)`;
                document.getElementById('speechBubble').classList.add('hidden');
            }

            function quickPoke() {
                const sprite = document.getElementById('spriteEmoji');
                sprite.classList.remove('anim-spin');
                void sprite.offsetWidth;
                sprite.classList.add('anim-spin');
                playTone("A5");
            }

            async function runCode() {
                if (isRunning || blocks.length === 0) return;
                isRunning = true;
                const container = document.getElementById('spriteContainer');
                const sprite = document.getElementById('spriteEmoji');
                const bubble = document.getElementById('speechBubble');
                const stage = document.getElementById('stageArea');

                const notes = ["C5", "D5", "E5", "G5", "A5", "C6"];

                for (let i = 0; i < blocks.length; i++) {
                    const stepEl = document.getElementById(`block-step-${i}`);
                    if (stepEl) stepEl.classList.add('ring-4', 'ring-yellow-300', 'scale-105');

                    const action = blocks[i].type;
                    sprite.className = 'text-7xl select-none filter drop-shadow-md';
                    void sprite.offsetWidth;

                    if (action === 'moveRight') {
                        posX = Math.min(posX + 55, 130);
                        container.style.transform = `translateX(${posX}px)`;
                        playTone("C5");
                    } else if (action === 'moveLeft') {
                        posX = Math.max(posX - 55, -130);
                        container.style.transform = `translateX(${posX}px)`;
                        playTone("D5");
                    } else if (action === 'jump') {
                        sprite.classList.add('anim-jump');
                        playTone("G5");
                    } else if (action === 'spin') {
                        sprite.classList.add('anim-spin');
                        playTone("E5");
                    } else if (action === 'sayHello') {
                        const phrases = ["Yay Aahana! 🌟", "Hello Friend! 💖", "Woohoo! 🎉", "Let's Dance! 🎶"];
                        bubble.innerText = phrases[Math.floor(Math.random() * phrases.length)];
                        bubble.classList.remove('hidden');
                        playTone("C6");
                    } else if (action === 'playMusic') {
                        sprite.classList.add('anim-dance');
                        playTone(notes[i % notes.length]);
                    } else if (action === 'changeBg') {
                        stage.classList.remove(...bgThemes[bgIndex].split(' '));
                        bgIndex = (bgIndex + 1) % bgThemes.length;
                        stage.classList.add(...bgThemes[bgIndex].split(' '));
                        playTone("B5");
                    }

                    await new Promise(r => setTimeout(r, 700));
                    if (stepEl) stepEl.classList.remove('ring-4', 'ring-yellow-300', 'scale-105');
                }

                setTimeout(() => bubble.classList.add('hidden'), 1500);
                isRunning = false;
            }

            renderBlocks();
        </script>
    </body>
    </html>
    """
    components.html(scratch_html, height=560, scrolling=False)

# ==========================================
# TAB 1: MAGIC BALLOON POP (Interactive Counter & Pop Effects)
# ==========================================
with tab1:
    st.header("🎈 Magic Balloon Pop")
    st.write("Tap the colorful balloons below to pop them and watch the counter grow!")

    if "balloon_score" not in st.session_state:
        st.session_state.balloon_score = 0

    col1, col2, col3, col4, col5 = st.columns(5)
    balloons = [
        ("🔴 Red", "pop_red"),
        ("🔵 Blue", "pop_blue"),
        ("🟢 Green", "pop_green"),
        ("🟡 Yellow", "pop_yellow"),
        ("🟣 Purple", "pop_purple"),
    ]

    for idx, (b_label, b_key) in enumerate(balloons):
        with [col1, col2, col3, col4, col5][idx]:
            if st.button(b_label, key=b_key, use_container_width=True):
                st.balloons()
                st.session_state.balloon_score += 1
                st.success(f"Pop! 🎉 ({b_label})")

    st.markdown(f"### 🏆 Total Pops: **{st.session_state.balloon_score}**")

    if st.button("🔄 Reset Balloons"):
        st.session_state.balloon_score = 0
        st.rerun()

# ==========================================
# TAB 2: FRUIT COUNTING (Interactive Math Game)
# ==========================================
with tab2:
    st.header("🍎 Fruit Counting Adventure")
    st.write("Count the fruits on the screen and tap the correct number!")

    if "target_count" not in st.session_state:
        st.session_state.target_count = random.randint(1, 5)
        st.session_state.fruit_score = 0

    target = st.session_state.target_count
    fruit_icon = random.choice(["🍎", "🍌", "🍓", "🍊", "🍇"])

    # Display row of fruits visually
    st.markdown(
        f"<h2 style='text-align: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>{fruit_icon * target}</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-weight: bold;'>How many fruits do you see?</p>",
        unsafe_allow_html=True,
    )

    btn_cols = st.columns(5)
    for i in range(1, 6):
        with btn_cols[i - 1]:
            if st.button(str(i), key=f"count_{i}", use_container_width=True):
                if i == target:
                    st.balloons()
                    st.success(
                        f"🌟 Correct! There are {target} {fruit_icon} fruits!"
                    )
                    st.session_state.fruit_score += 1
                    st.session_state.target_count = random.randint(1, 5)
                    st.rerun()
                else:
                    st.error("❌ Not quite! Try counting again.")

    st.markdown(f"**Score:** {st.session_state.fruit_score} 🎯")

# ==========================================
# TAB 3: ANIMAL SOUND BOX (Interactive Audio-Visuals)
# ==========================================
with tab3:
    st.header("🦁 Animal Sound Box")
    st.write("Tap your favorite animal to hear what they say!")

    animal_cols = st.columns(4)
    animals = [
        {"name": "Lion", "emoji": "🦁", "sound": "Roar! 🦖"},
        {"name": "Cow", "emoji": "🐮", "sound": "Moo! 🥛"},
        {"name": "Duck", "emoji": "🦆", "sound": "Quack Quack! 🌊"},
        {"name": "Dog", "emoji": "🐶", "sound": "Woof Woof! 🦴"},
    ]

    for idx, animal in enumerate(animals):
        with animal_cols[idx]:
            if st.button(
                f"{animal['emoji']}\n{animal['name']}",
                key=f"animal_{idx}",
                use_container_width=True,
            ):
                st.snow()
                st.markdown(
                    f"<div style='text-align: center; padding: 15px; background-color: #e6f4ea; border-radius: 10px;'>"
                    f"<h2>{animal['emoji']} The {animal['name']}</h2>"
                    f"<h3>Says: <b>{animal['sound']}</b></h3>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

# ==========================================
# TAB 4: COLOR MATCHER (Interactive Color Game)
# ==========================================
with tab4:
    st.header("🎨 Color Matching Challenge")
    st.write("Find and click the matching color name!")

    if "color_target" not in st.session_state:
        st.session_state.color_target = random.choice(
            ["Red", "Blue", "Green", "Yellow"]
        )
        st.session_state.color_score = 0

    c_target = st.session_state.color_target
    st.markdown(
        f"<h3 style='text-align: center;'>Can you find the box for: <span style='color: #ff4b4b; font-size: 1.2em;'>{c_target}</span>?</h3>",
        unsafe_allow_html=True,
    )

    cc1, cc2, cc3, cc4 = st.columns(4)

    colors_list = [
        ("🔴 Red", "Red", cc1),
        ("🔵 Blue", "Blue", cc2),
        ("🟢 Green", "Green", cc3),
        ("🟡 Yellow", "Yellow", cc4),
    ]

    for label, col_name, col_obj in colors_list:
        with col_obj:
            if st.button(label, key=f"col_btn_{col_name}", use_container_width=True):
                if col_name == c_target:
                    st.balloons()
                    st.success("🎉 Awesome job matching the color!")
                    st.session_state.color_score += 1
                    st.session_state.color_target = random.choice(
                        ["Red", "Blue", "Green", "Yellow"]
                    )
                    st.rerun()
                else:
                    st.error("Oops! Try another color.")

    st.markdown(f"**Score:** {st.session_state.color_score} 🌈")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ for Aahana | Streamlit Interactive Play Zone & Scratch Studio</p>",
    unsafe_allow_html=True,
)
