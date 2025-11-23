# 🌟 K-Pop Vibe Check: Content-Based Recommendation Engine

This is a live prototype demonstrating full-stack data application development, designed to help users filter and rank content based on aesthetic preference and custom scoring algorithms.

## 🚀 Live Application

🔗 **Access the Live App Here:** [PASTE YOUR STREAMLIT CLOUD URL HERE]

## 💡 The Problem & Solution

**The Problem:** Standard recommendation systems often use rigid filters (e.g., genre or album sales) and fail to capture nuanced user preferences like aesthetic or 'vibe'.

**The Solution:** I built an engine that allows users to filter data by categories (e.g., 'Dark Academia') and then rank the results using a **custom, weighted algorithm** (60% Charisma + 40% Visuals), providing a truly personalized recommendation.

---

## 🛠️ Key Technical Features

This project demonstrates proficiency in the full software development lifecycle:

* **Custom Ranking Logic:** Implemented **weighted scoring algorithms** using Python **`lambda` functions** for dynamic ranking.
* **Data Management (CRUD):** Utilized Streamlit **`st.session_state`** to implement **CRUD (Create, Read, Update, Delete)** functionality, allowing users to dynamically add new data to the live database via an **`st.form`**.
* **Full UI/UX Control:** Achieved advanced visual customization, including dynamic **theme switching** and targeted element styling using **CSS Injection** (`st.markdown` with `unsafe_allow_html=True`).
* **Data Proficiency:** Used **List Comprehension** for efficient data filtering.

---

## ⚙️ How to Run Locally

If you want to run this application on your own machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/kpop-recommendation-engine.git](https://github.com/YOUR_USERNAME/kpop-recommendation-engine.git)
    ```
2.  **Navigate to the folder:**
    ```bash
    cd kpop-recommendation-engine
    ```
3.  **Install Requirements:** (Requires Python and pip)
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
