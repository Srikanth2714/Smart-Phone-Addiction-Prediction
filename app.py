import pickle
import streamlit as st
import pandas as pd

# Apply background image
def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Initialize session state for login and user storage
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "users" not in st.session_state:
    try:
        with open("users.pkl", "rb") as f:
            st.session_state["users"] = pickle.load(f)
    except FileNotFoundError:
        st.session_state["users"] = {"admin": "admin123"}  # Default user

# Function to save user data
def save_users():
    with open("users.pkl", "wb") as f:
        pickle.dump(st.session_state["users"], f)

# Function for login page
def login_page():
    set_bg("https://source.unsplash.com/1600x900/?technology,login")  # Background image for login page
    
    st.markdown("""
    <h1 style="display: inline; font-size: 36px; color: white;">📱 Smartphone Addiction Predictor</h1>
    """, unsafe_allow_html=True)
    st.subheader("🔐 Login to Continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["logged_in"] = True
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")
    
    if st.button("⬅️ Back"):
        st.session_state["show_register"] = False
        st.rerun()

    if st.button("Don't have an account? Register here"):
        st.session_state["show_register"] = True
        st.rerun()

# Function for registration page
def register_page():
    set_bg("https://source.unsplash.com/1600x900/?register,signup")
    st.title("📝 Register")
    st.subheader("Create a new account")

    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_username in st.session_state["users"]:
            st.error("❌ Username already exists! Try a different one.")
        elif new_password != confirm_password:
            st.error("❌ Passwords do not match!")
        else:
            st.session_state["users"][new_username] = new_password
            save_users()
            st.success("✅ Registration successful! Please log in.")
            st.session_state["show_register"] = False
            st.rerun()
    
    if st.button("⬅️ Back"):
        st.session_state["show_register"] = False
        st.rerun()

# Show Register or Login Page
if "show_register" in st.session_state and st.session_state["show_register"]:
    register_page()
    st.stop()

if not st.session_state["logged_in"]:
    login_page()
    st.stop()

# ========== Main App (Smartphone Addiction Predictor) ==========
set_bg("https://source.unsplash.com/1600x900/?smartphone,technology")

st.markdown("""
    <h1 style="display: inline; font-size: 36px; color: white;">📱 Smartphone Addiction Predictor</h1>
""", unsafe_allow_html=True)
st.markdown("<h3 style='color: white;'>Choose either 1 (Yes) or 0 (No):</h3>", unsafe_allow_html=True)

# Load the trained model
with open('multiple_models.pkl', 'rb') as file:
    model = pickle.load(file)

# Define all 18 questions
questions = [
    "Do you use your phone to click pictures of class notes?",
    "Do you buy books/access books from your mobile?",
    "Does your phone's battery last a day?",
    "When your phone's battery dies out, do you run for the charger?",
    "Do you worry about losing your cell phone?",
    "Do you take your phone to the bathroom?",
    "Do you check your phone immediately after waking up?",
    "Do you use your phone while eating meals?",
    "Do you feel anxious when your phone is not near you?",
    "Do you spend more time on your phone than talking to people?",
    "Do you use your phone before going to sleep?",
    "Do you feel restless if you don’t use your phone for a while?",
    "Do you prefer texting over calling?",
    "Do you use your phone in social gatherings?",
    "Do you check notifications even when there are none?",
    "Do you feel your productivity is reduced due to phone usage?",
    "Do you experience eye strain from excessive phone use?",
    "Do you feel the urge to check your phone during work or study?"
]

# Collect user inputs
input_features = [st.selectbox(q, [1, 0]) for q in questions]

# Prediction button
if st.button("Predict"):
    prediction = model.predict([input_features])[0]
    
    if prediction == 1:
        st.error("🔴 You are likely addicted to your smartphone. 📵 Try reducing screen time!")
        st.markdown("""
        **Tips to Reduce Smartphone Addiction:**
        - 📵 Set screen time limits using apps like Digital Wellbeing or Screen Time.
        - 🚫 Avoid using your phone right before sleep.
        - 👥 Engage in offline activities like reading, exercise, or socializing.
        - ⏳ Take frequent breaks from screens.
        - 🔕 Disable non-essential notifications.
        - ⏰ Use a real alarm clock instead of your phone.
        """)
    else:
        st.success("🟢 You are not addicted to your smartphone. Keep up the good habits! ✅")

# Sidebar for additional info
with st.sidebar:
    st.markdown("## Navigation")

    if st.button("About"):
        st.title("📌 About the Project")
        st.write("""
        **📱 Smart Phone Addiction Prediction**  
        This project predicts smartphone addiction levels based on behavioral patterns and psychological responses.
        """)

    if st.button("Algorithms Used"):
        st.title("📌 Machine Learning Models Used")
        st.write("""
        - **Random Forest** 🌲: A collection of decision trees that work together to improve prediction accuracy.
        - **Decision Tree** 🌳: A simple but powerful algorithm that splits data into nodes for classification.
        - **Gradient Boosting** 🚀: An ensemble method that builds models sequentially, correcting errors along the way.
        - **SVM (Support Vector Machine)** 📈: Finds the optimal boundary to classify data.
        - **XGBoost & AdaBoost** ⚡: Advanced boosting techniques that enhance weak models.
        - **Artificial Neural Networks (ANN)** 🧠: A deep learning model inspired by the human brain.
        """)

    if st.button("Dataset"):
        df = pd.read_csv('20250210102359smart-phone-dataset.csv')
        st.dataframe(df)

    if st.button("⬅️ Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
