from crewai import Agent, Task, Process, Crew
from agents import Agents 
from tools import search_tool


class Tasks:
    def __init__(self, event, language):
        self.information_note = event
        self.gbook_note = event
        self.language = language

    def information_task(self):
        search_task = Task(

            description = f"""
                Search information based on {self.information_note} using [search_tool] information related to https://gaeni.org/ site if information gathered is not relevant  enaough search from other site
                The gema specialist at GEMA FOUNDATION is responsible for gathering, organizing, and curating relevant information related to technopreneur, front end back end, sourcing data, artificial intelligence, story telling, metaverse, legal aspect HKKI, research findings, and policy reports to support GEMA’s goals of improving education in Indonesia through innovation and technology. The specialist will collaborate with departments to understand specific information needs and ensure accuracy and relevance in the data retrieved.and sustainable development. This includes sourcing scientific data, research findings, and policy reports to support GEMA FOUNDATION`S mission of addressing key challenges in technology. The specialist will collaborate with research teams and departments to understand specific information needs and utilize advanced retrieval systems and algorithms to ensure accuracy and relevance of the data retrieved. Key responsibilities include:
                - Conduct efficient keyword and semantic searches across multiple platforms, focusing on storytelling, front end back end, artificial intelligence, technopreneur.
                - Analyze and summarize technology research.
                - Validate the credibility of data sources, ensuring that the information is aligned with GEMA FOUNDATION's mission and is reliable for academic and policy use.""",
            expected_output = f"""A comprehensive language {self.language} report covers everything:
                            - - Data Summary, make sure to use {self.language}.
                            - Source Citations.
                            - Recommendations.""", 
            agent=Agents().information_agent(), 
            tools=[search_tool]
        )
        return search_task
    
    def gbook_task(self):
        gbook_task = Task(
            description= f"""
                search information based on {self.gbook_note} using [seaarch_tool] information related to https://gbook.gaeni.org site if information gathered is not relevant enaough search from other site
                your gbook should include:
                - Relevant information from user query from G-Book.
                - Analyze and learn more about G-Book Gema Foundation""",
            expected_output= f"""A comprehensive language {self.language} report covers everything:
                            - Data Summary, make sure to use {self.language}.
                            - Relevant information from the Ebook concerning user questions.
                            - provides links to recommended books to read related to the context of the user's question.
                            - Analyze, summarize the G-Book Gema Foundation's and give the link G-Book.""",
            agent=Agents().gbook_agent(),
            tools=[search_tool]
        )
        return gbook_task
