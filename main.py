from dotenv import load_dotenv
load_dotenv()
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

from typing import List
from pydantic import BaseModel, Field



# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches the web for the given query.
#     Args:
#         query (str): The query to search for.
#     Returns:
#         str: The search results.
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)

class Source(BaseModel):
    """Schema for a source used by an agent """
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Shema for agent response with answer and sources"""

    answer:str = Field(description="the agent's answer to the query")
    source: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")




llm = ChatOpenAI(temperature=0, model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model = llm, tools = tools, response_format=AgentResponse)


def main():
    print("Hello from project!")
    result = agent.invoke({'messages': [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]} )
    print(result)

if __name__ == "__main__":
    main()
