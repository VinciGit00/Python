import os
from dotenv import load_dotenv
from scrapegraph_py.scrape import scrape
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from IPython.display import Image, display

load_dotenv()

def smart_scraper_func(prompt: str, source: str, key: str):
    """
    Performs intelligent scraping using SmartScraperGraph, a powerful tool designed to extract 
    relevant information from web pages based on user-defined prompts. This function leverages 
    the capabilities of the SmartScraperGraph API to retrieve structured data from the specified 
    source URL, making it ideal for applications that require automated data collection.

    Parameters:
    prompt (str): A user-defined string that specifies the type of information to extract from 
                  the source. This prompt guides the scraping process and can include specific 
                  instructions or keywords to refine the results.
    source (str): The URL of the web page from which data is to be scraped. This should be a 
                  valid and accessible URL that contains the information relevant to the prompt.
    key (str): The API key required for authentication with the SmartScraperGraph service. 
               This key is essential for accessing the scraping functionality and should be kept 
               secure.

    Returns:
    dict: A dictionary containing the result of the scraping operation in JSON format. The 
          dictionary includes the extracted data structured according to the prompt provided. 
          The exact structure of the returned data may vary based on the content of the source 
          and the specificity of the prompt.

    Example:
    >>> result = smart_scraper_func('Extract article titles', 'https://example.com', 'your_openai_key')
    >>> print(result)
    """
    result = scrape(key, source, prompt)
    return result

api_key = os.getenv("GPT4O_API_KEY")

tools = [smart_scraper_func]
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing scraping scripts with scrapegraphai")

def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()

display(Image(react_graph.get_graph(xray=True).draw_mermaid_png()))
