import os
from dotenv import load_dotenv
import streamlit as st
from streamlit.components.v1 import html
from langchain_openai import ChatOpenAI
from crewai import Process, Crew
import base64
from agents import Agents
from tasks import Tasks
from tools import *

load_dotenv()

def main():
    st.set_page_config(
        page_title="GAENI AI",
        page_icon="Logo/Logo_GEMA.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as file:
            binary_data = file.read()
            base64_data = base64.b64encode(binary_data).decode('utf-8')
        return base64_data

    # Load and display logo
    logo_path = "./Logo/Logo_GEMA.png"
    logo_base64 = get_base64_of_bin_file(logo_path)

    # Load CSS file for custom styling
    with open("style.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

    # Display header with logo and welcome message
    st.markdown(f"""
        <div class="header">
            <img src="data:image/png;base64,{logo_base64}" class="Logo">
            <p>Welcome to GAENI AI</p>
        </div>
    """, unsafe_allow_html=True)

    # Input section for user question and language selection
    question = st.text_area("Hello GAENI AI ready to help you", placeholder="Write your question here")
    language = st.selectbox("Select output language:",
                            ("Choose Language...", "Indonesian", "English", "German", "Japanese", "Mandarin"))
    st.write(f"**Your Question:** {question}")

    # Initialize the OpenAI GPT model
    openaigpt4 = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.2,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Set up Crew agents and tasks with selected language
    information_crew = Crew(
        agents=[Agents().information_agent(), Agents().gbook_agent()],
        tasks=[Tasks(question, language).information_task(), Tasks(question, language).gbook_task()],
        process=Process.sequential,
        manager_llm=openaigpt4
    )

    # Button to start the search process
    if st.button("Search"):
        with st.spinner("Searching for answers..."):
            results = information_crew.kickoff()

        # Display results with custom styling
        st.markdown(f"""
            <div class="answer">
                **Answer:**
                {results}
            </div>
        """, unsafe_allow_html=True)

        st.success("Results saved successfully!")

if __name__ == "__main__":
    main()
