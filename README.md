# 🧠 AI Resume & Portfolio Builder (Streamlit + Gemini)

This application is a simple, yet powerful web tool built with **Streamlit** and **Google Gemini** that automates the creation of professional resume summaries and cover letters. By inputting your project details, skills, and career goals, the Gemini API generates polished, action-oriented content ready for your job application.

---

## ✨ Features

* **Intelligent Content Generation:** Uses the `gemini-2.5-flash` model to transform raw inputs (skills, project descriptions, goals) into professional, targeted resume language.
* **Targeted Output:** Generates both a concise **Resume Summary** (3-4 lines) and a customizable **Cover Letter** draft.
* **Easy-to-Use Interface:** Streamlit provides a clean, interactive user interface for quick data entry and content generation.
* **One-Click Download:** Generated content can be downloaded instantly as a `.txt` file.

---

## 🛠️ Prerequisites

Before running this application, you need to ensure you have the following installed and configured:

1.  **Python 3.8+**
2.  **Gemini API Key:** Obtain a key from Google AI Studio.

### Installation

1.  **Clone the repository (or download the file):**
    ```bash
    git clone [YOUR_REPO_URL_HERE]
    cd ai-resume-builder
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install streamlit google-genai
    ```

---

## 🚀 How to Run the App

1.  **Set Your API Key:**
    * Open the `new ai resume2.py` file.
    * Replace the placeholder value for `GEMINI_API_KEY` with your actual key:
        ```python
        GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE" 
        ```
    **(Optional but Recommended):** For better security, consider loading your API key from a Streamlit secrets file (`.streamlit/secrets.toml`) instead of hardcoding it.

2.  **Launch the Streamlit Application:**
    Open your terminal or PowerShell window in the same directory as the script and run:
    ```bash
    streamlit run "new ai resume2.py"
    ```
    This command will automatically open the application in your default web browser (usually at `http://localhost:8501`).

---

## 📝 Usage

1.  **Input Your Details:** Fill out the input fields in the Streamlit interface:
    * Your Name
    * Target Job Title
    * List of Key Skills (comma-separated)
    * Detailed Project/Experience Description
    * Your Career Goals/Motivation
2.  **Generate Content:** Click the **`🚀 Generate Resume & Cover Letter`** button.
3.  **Review and Download:** The AI-generated summary and cover letter will appear instantly under the **Generated Content** section, ready to be copied or downloaded.

---

## 📄 File Structure
---

## 🤝 Contribution

Feel free to fork this project, submit pull requests, or open issues if you find bugs or have suggestions for new features (e.g., adding a 'Work Experience' section or different generation models).

---

## 🧑‍💻 Built By

**Libna** (Your Name)
* [Link to your LinkedIn]
* [Link to your Portfolio/Website]

---






