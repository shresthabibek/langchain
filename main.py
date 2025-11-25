from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch


load_dotenv()

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




llm = ChatOpenAI(temperature=0, model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model = llm, tools = tools)


def main():
    print("Hello from project!")
    result = agent.invoke({'messages': [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]} )
    print(result)

if __name__ == "__main__":
    main()
