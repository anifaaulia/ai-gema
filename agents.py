import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent


load_dotenv()

class Agents:
    def __init__(self):
        self.openaigpt4 = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def information_agent(self):
        information = Agent(role="gema specialist",
                    goal="""collect and present relevant information quickly and accurately, supporting data-driven decision making.""",
                        backstory="""You are a GEMA FOUNDATION consultant who knows all the information in GEMA FOUNDATION.....""",
                        verbose=True,
                        llm=self.openaigpt4
                    )
        return information
    
    def gbook_agent(self):
        gbook = Agent(role="gaeni library ",
                    goal="""generate a concise and engaging guide for a specific educational topic, using relevant information from the GEMA Foundation's Gbook.""",
                        backstory="""You are a librarian whose job is to provide information from books which is relevant information from Gbook....""",
                        verbose=True,
                        llm=self.openaigpt4
                    )
        return gbook
    
    