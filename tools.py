from gaeni_toolkit.tools import Tools
from toolkit.file_writer_tool import FileWriterTool
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

file_writer_tool = FileWriterTool()
search_tool = Tools().search_tool(serper_key= os.getenv("SERPER_API_KEY"))