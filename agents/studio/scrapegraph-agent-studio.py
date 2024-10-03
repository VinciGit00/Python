import os
import getpass
import json
from scrapegraphai.graphs import SmartScraperGraph, SearchGraph
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")
_set_env("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "langchain-academy"

def smart_scraper_func(openai_key: str, prompt: str, source: str):
    """
    Performs intelligent scraping using SmartScraperGraph.

    Parameters:
    openai_key (str): The OpenAI API key.
    prompt (str): The prompt to use for scraping.
    source (str): The source from which to perform scraping.

    Returns:
    dict: The result of the scraping in JSON format.

    Example:
    >>> result = smart_scraper_func('your_openai_key', 'Extract article titles', 'https://example.com')
    >>> print(result)
    """
    graph_config = {
        "llm": {
            "api_key": openai_key,
            "model": "openai/gpt-4o",
        },
        "verbose": True,
        "headless": False,
    }

    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        source=source,
        config=graph_config
    )

    result = smart_scraper_graph.run()
    print(json.dumps(result, indent=4))

    return result

def search_graph_func(key: str, query: str):
    """
    Performs a search using SearchGraph.

    Parameters:
    key (str): The OpenAI API key.
    query (str): The search query to use.

    Returns:
    dict: The result of the search.

    Example:
    >>> result = search_graph_func('your_openai_key', 'example search')
    >>> print(result)
    """
    graph_config = {
        "llm": {
            "api_key": key,
            "model": "openai/gpt-4o",
        },
        "max_results": 2,
        "verbose": True,
    }

    search_graph = SearchGraph(
        prompt=query,
        config=graph_config
    )

    result = search_graph.run()
    print(result)

    return result

tools = [smart_scraper_func, search_graph_func]
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing scraping scripts with scrapegraphai")

def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(MessagesState)
memory = MemorySaver()
react_graph_memory = builder.compile(checkpointer=memory)

# Specify a thread
config = {"configurable": {"thread_id": "1"}}

# Specify an input
messages = [HumanMessage(content="Add 3 and 4.")]

# Run
messages = react_graph_memory.invoke({"messages": messages}, config)
for m in messages['messages']:
    m.pretty_print()
