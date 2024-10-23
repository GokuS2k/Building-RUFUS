# Rufus for RAG context

## Req:
- python, Selenium, Bs4, any web driver (ex: Chrome Driver)

## Installation procedure:
- Install the packages: pip install selenium beautifulsoup4 requests
- Download and install the driver which matches the browser's version
- Place the <driver>.exe file in a directory and either provide the full path in the code (like how I did) or add the driver to your system's PATH variable.

## Usage:
- Go to directory where you have installed this code, and run this cmd: python Rufus.py
- You will see the results in the same directory by the name: RUFUS_results.json
- In the main(), we initialize the RufusforRAG client with an API key, perform a Google search, and save the structured results in a JSON file.
- You could modify the search query (q) if needed.
