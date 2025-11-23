import streamlit as st
# --- THEME CSS DEFINITIONS ---
THEME_CSS = {
    'Pastel Pop': """
        <style>
        .stApp {
            background-color: #f5abbd; /* Alice Blue */
            color: #000000
        }
        label {
        color: #000000 !important; /* Forces label text to black */
    }
        </style>
    """,

    'Dark Academia': """
        <style>
        .stApp {
            background-color: #543a32; /* Dark Slate */
            color: #E0E0E0; /* Light text */
        }
        </style>
    """,
    'Soft Grunge': """
        <style>
        .stApp {
            background-color: #2d382a; /* Darker Green/Gray */
            color: #ffffff
        }
        </style>
    """,
    
    # Add more themes here!
}
# --- New Code Block: The Expanded Idol Dataset ---
# --- SESSION STATE INITIALIZATION (The App's Memory) ---
if 'idol_data_list' not in st.session_state:
    st.session_state['idol_data_list'] = [
        # PASTE YOUR COMPLETE LIST OF IDOL DICTIONARIES HERE
        {"name": "V", "group": "BTS", "aesthetic": "Dark Academia", "visuals": 9.5, "charisma": 9.8},
    {"name": "Jimin", "group": "BTS", "aesthetic": "Soft Grunge", "visuals": 9.7, "charisma": 9.3},
    {"name": "Karina", "group": "Aespa", "aesthetic": "Pastel Pop", "visuals": 9.9, "charisma": 9.0},
    {"name": "Suga", "group": "BTS", "aesthetic": "Soft Grunge", "visuals": 8.5, "charisma": 9.9},
    {"name": "Hoshi", "group": "SEVENTEEN", "aesthetic": "Pastel Pop", "visuals": 9.2, "charisma": 9.7},
    {"name": "Woozi", "group": "SEVENTEEN", "aesthetic": "Soft Grunge", "visuals": 8.8, "charisma": 9.6},
    {"name": "Joshua", "group": "SEVENTEEN", "aesthetic": "Dark Academia", "visuals": 9.8, "charisma": 9.6},
    {"name": "Haechan", "group": "NCT", "aesthetic": "Dark Academia", "visuals": 9.2, "charisma": 9.5},
    {"name": "Han", "group": "Stray Kids", "aesthetic": "Soft Grunge", "visuals": 8.9, "charisma": 9.6},
    {"name": "Ricky", "group": "ZB1", "aesthetic": "Pastel Pop", "visuals": 9.5, "charisma": 9.5},
    {"name": "Jake", "group": "ENHYPEN", "aesthetic": "Dark Academia", "visuals": 9.6, "charisma": 9.6},
    {"name": "Taehyun", "group": "TXT", "aesthetic": "Pastel Pop", "visuals": 9.3, "charisma": 9.4},
    {"name": "Yeosang", "group": "ATEEZ", "aesthetic": "Dark Academia", "visuals": 9.6, "charisma": 9.2},
    {"name": "Niki", "group": "ENHYPEN", "aesthetic": "Soft Grunge", "visuals": 9.2, "charisma": 9.6}

        # ... all 14 idols ...
    ]
# --- END SESSION STATE ---
# --- End New Code Block ---
# --- End New Code Block ---

# --- New Code Block at the Top ---

# 1. Your AI Product Designer Sidebar
st.sidebar.title("App Settings 🛠️")
st.sidebar.markdown("Use this to fine-tune your aesthetic.")

# 2. Sidebar Element - Practice with New UI
aesthetic = st.sidebar.radio(
    "Choose Aesthetic:",
    ['Pastel Pop', 'Dark Academia', 'Soft Grunge']
)
# --- New Code Block: Sorting Control ---
st.sidebar.markdown("---") # Adds a nice separator
sort_by = st.sidebar.radio("Rank Idols By:", ['Visuals', 'Charisma' , 'Overall score'])
# --- End New Code Block ---

# --- End New Code Block ---

# 1. Configure the page title and icon
st.set_page_config(page_title="K-Pop Vibe Check", page_icon="💜")

# 2. Add a title with your aesthetic
st.title("💜 Welcome to the K-Pop Zone")

# 3. Interactive Element

# --- New Code Block ---

# 1. New UI Element: a Selectbox (dropdown)
mood = st.selectbox(
    "How are you feeling right now? Select your mood:", 
    ["Select Mood", "Hype / Energetic", "Sad / Reflective", "Need to Study / Focus"]
)

# 2. Python Logic (The "Brain")
if mood == "Hype / Energetic":
    st.header("⚡ Hype Recommendation!")
    st.write("Go listen to **NewJeans - Super Shy** while dancing badly in your room.")
elif mood == "Sad / Reflective":
    st.header("😌 Reflective Vibe.")
    st.write("Listen to **BTS - Spring Day** and drink some hot cocoa. You got this.")
elif mood == "Need to Study / Focus":
    st.header("📚 Study Time!")
    st.write("Put on a **lo-fi K-pop playlist** and tackle that AIML problem set. Fighting!")
elif mood != "Select Mood":
    # Fallback for any other mood you might add later
    st.info("I need to learn more about that feeling! For now, try Blackpink's 'Pink Venom'.")

# --- End New Code Block ---

# --- New Code Block: Image Logic ---

# We'll use the aesthetic choice from your sidebar!
st.subheader(f"Current Aesthetic Vibe: {aesthetic}")

# Simple IF/ELIF logic to display an image URL based on the aesthetic
if aesthetic == 'Pastel Pop':
    st.image("https://i.pinimg.com/736x/1d/78/d7/1d78d72c1e9b5426b5ee79057bf57b70.jpg", caption="Pastel Pop Vibe")

elif aesthetic == 'Dark Academia':
    st.image("https://i.pinimg.com/736x/34/4e/f7/344ef70113b21ecf493f0d3ee699cb0a.jpg", caption="Dark Academia Vibe")
elif aesthetic == 'Soft Grunge':
    st.image("https://i.pinimg.com/736x/ba/e3/83/bae38365aa9dca16fb5dbecc1640e554.jpg", caption="Soft Grunge Vibe")
else:
    st.warning("Please choose an aesthetic from the sidebar!")
# --- DYNAMIC INJECTION CODE ---

# 1. Get the CSS string based on the user's choice
selected_css = THEME_CSS.get(aesthetic, "") 

# 2. Inject the CSS into the page
st.markdown(selected_css, unsafe_allow_html=True) 

# --- END DYNAMIC INJECTION CODE ---

# --- End New Code Block ---

# --- New Code Block: Data Filtering Logic ---

st.header("Idols Matching Your Aesthetic:")

# 1. Python List Comprehension (A core Data Skill!)
matching_idols = [
    idol for idol in st.session_state['idol_data_list'] if idol["aesthetic"] == aesthetic
]

# 2. Display the filtered results
# --- Replacement Code Block: Ranking Logic ---

st.header(f"Idols Matching {aesthetic}, Ranked by {sort_by}:")

# --- Modifying the Ranking Logic Block ---

# --- REPLACE THE ENTIRE RANKING LOGIC BLOCK (STARTING FROM 'if matching_idols:') ---

if matching_idols:
    # 1. Check what the user selected in the sidebar
    if sort_by == 'Overall score': 
        # *This code runs ONLY when 'Overall Score' is selected.*
        # It calculates your weighted average (60% Charisma, 40% Visuals)
        ranked_idols = sorted(
            matching_idols, 
            key=lambda x: (0.6 * x['charisma']) + (0.4 * x['visuals']), 
            reverse=True
        )
    else:
        # *This code runs for 'Visuals' or 'Charisma'.*
        # It uses the simple key lookup that works for the existing data.
        ranked_idols = sorted(
            matching_idols, 
            key=lambda x: x[sort_by.lower()], 
            reverse=True
        )
    
    # Display the final, ranked table
    st.dataframe(ranked_idols, use_container_width=True)

# --- END OF REPLACEMENT BLOCK ---# --- End Replacement Code Block ---
# --- End New Code Block ---

# --- ADD NEW IDOL FORM (Goes at the very end of your app.py) ---

with st.form("new_idol_form", clear_on_submit=True):
    st.header("➕ Contribute to the Database")
    
    # Form Inputs
    new_name = st.text_input("Idol Name")
    new_group = st.text_input("Group Name")
    new_aesthetic = st.selectbox("Aesthetic", ['Pastel Pop', 'Dark Academia', 'Soft Grunge'])
    new_visuals = st.slider("Visuals Score (1-10)", 1.0, 10.0, 5.0, 0.1)
    new_charisma = st.slider("Charisma Score (1-10)", 1.0, 10.0, 5.0, 0.1)

    submitted = st.form_submit_button("Add Idol to Database")
    
    if submitted:
        # Create the new dictionary object
        new_entry = {
            "name": new_name, 
            "group": new_group, 
            "aesthetic": new_aesthetic, 
            "visuals": new_visuals, 
            "charisma": new_charisma
        }
        
        # Append the new entry to the data stored in memory
        st.session_state['idol_data_list'].append(new_entry)
        
        st.success(f"Added {new_name} to the database! Check the table above.")

# --- END FORM ---