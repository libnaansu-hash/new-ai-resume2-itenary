import streamlit as st
import google_genai as genai
from google.genai.errors import APIError

# --- 1. Configuration and Client Initialization ---

# IMPORTANT: Replace the placeholder with your actual Gemini API Key
# Best practice is to use st.secrets or environment variables, but for this example:
GEMINI_API_KEY = "YOUR_API_KEY" 
# NOTE: The provided key is a placeholder and will not work.

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    # This prevents the app from crashing if the client fails to initialize
    st.error(f"Error initializing Gemini client. Please check your API key: {e}")
    client = None

# --- 2. Define the AI generation function ---

def generate_resume_content(client: genai.Client, name: str, skills: str, projects: str, goals: str, job_title: str) -> str:
    """Generates professional resume content using the Gemini API."""
    
    prompt = f"""
    You are an expert resume writer. Create a professional resume summary and cover letter for:
    Name: {name}
    Skills: {skills}
    Projects: {projects}
    Career Goals: {goals}
    Target Job Title: {job_title}

    Format your output clearly with headings:
    ### 1. Resume Summary (3-4 lines)
    [Summary Text Here]

    ### 2. Cover Letter
    [Cover Letter Text Here]
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={"temperature": 0.7}
        )
        # The content attribute holds the generated text
        return response.text
    except APIError as e:
        return f"🚨 API Error: Failed to generate content. Check your API key and permissions. Details: {e}"
    except Exception as e:
        return f"🚨 An unexpected error occurred: {e}"
# --- 3. Build the Streamlit UI ---

st.set_page_config(page_title="AI Resume Builder", page_icon="🧾")
st.title("🧠 AI Resume & Portfolio Builder")
st.markdown("Generate a professional resume summary and cover letter using Gemini AI.")

# Input fields
st.subheader("Input Your Details")
name = st.text_input("Your Name", "CHAKK")
job_title = st.text_input("Target Job Title (e.g., Data Science Intern)", "Data Science Intern")
skills = st.text_area("List Your Key Skills (e.g., Python, Pandas, SQL, Communication)", "Python, Scikit-learn, Pandas, Matplotlib, SQL")
projects = st.text_area("Describe Your Best Project/Experience (e.g., Built a predictive house pricing model...)", "Built a model to predict house prices, cleaned data, and achieved 8% error rate.")
goals = st.text_area("Your Career Goals/Motivation", "To secure a challenging internship and apply machine learning skills to solve business problems.")


# Generate button
if st.button("🚀 Generate Resume & Cover Letter"):
    # Check if client is initialized and all required fields are filled
    if not client:
        st.error("Cannot connect to AI. Please check the API key in the script.")
    elif name and skills and projects and goals and job_title:
        with st.spinner("Generating content with Gemini AI..."):
            output = generate_resume_content(client, name, skills, projects, goals, job_title)
        
        st.subheader("📝 Generated Content")
        st.markdown(output)
        
        # Download Option
        st.download_button(
            label="Download as Text File",
            data=output,
            file_name=f'{job_title.replace(" ", "_")}_AI_Content.txt',
            mime='text/plain',
        )

    else:
        st.warning("Please fill in all fields before generating.")

# Footer
st.markdown("---")

st.caption("Built by CHAKK • Powered by Gemini AI & Streamlit")




