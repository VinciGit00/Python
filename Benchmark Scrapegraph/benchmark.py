""" 
Basic example of scraping pipeline using SmartScraper
"""
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        # "model_tokens": 2000, # set context length arbitrarily,
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    }
}

# Test 1
print("test 1")
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    # also accepts a string with the already downloaded HTML code
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Test 2
print("test 2")
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the articles with their description.",
    # also accepts a string with the already downloaded HTML code
    source="https://www.wired.com",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Test 3
print("test 3")
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the articles with their the costs and image url.",
    # also accepts a string with the already downloaded HTML code
    source=" https://www.amazon.it/s?k=alexa&__mk_it_IT=ÅMÅŽÕÑ&crid=1WWVF1RGDBBSB&sprefix=alex%2Caps%2C114&ref=nb_sb_noss_2",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
