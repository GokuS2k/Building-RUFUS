# Rufus for RAG context (Rufus.py)

## Req:
- python, Selenium, Bs4, any web driver (ex: Chrome Driver)

## Installation procedure:
- Install the packages: pip install selenium beautifulsoup4 requests
- Download and install the driver which matches the browser's version
- Place the *driver*.exe file in a directory and either provide the full path in the code (like how I did) or add the driver to your system's PATH variable.

## Usage:
- Go to directory where you have installed this code, and run this cmd: python Rufus.py
- You will see the results in the same directory by the name: RUFUS_results.json
- In the main(), we initialize the RufusforRAG client with an API key, perform a Google search, and save the structured results in a JSON file.
- You could modify the search query (q) if needed.

## Submission requirements:
- Summary of the approach and blockers on the way: I initially started coding in Google Colab, which presented several challenges, particularly with running ChromeDriver in a cloud environment. Despite multiple attempts to resolve browser compatibility issues, the process became inefficient. After considerable effort, I transitioned to my local IDE (VSCode), where I was able to configure ChromeDriver. This change allowed me to focus more on refining the core functionality of Rufus, such as performing Google searches, extracting data, and structuring it in JSON format. The local environment ultimately provided the stability and control needed to complete the project efficiently.
- How it works: Rufus automates web scraping by performing Google searches based on user queries. It extracts titles, links, and descriptions from search results and structures them into a JSON format. The tool can be easily integrated into a Retrieval-Augmented Generation (RAG) pipeline, where the structured web data can serve as a knowledge source for LLMs. The client is initialized with an API key, performs the search, and stores the results in a JSON file, making it accessible for downstream RAG systems.

## How to run RUFUS agent for Retrieval augmented generation (RAG):
'''
from RufusforRAG import RufusforRAG
import os

def main():
    key = os.getenv('Rufus_API_KEY') # Get key from.env file
    client = RufusforRAG(key)
    prompt = "What is...?" # Enter your prompt
    results = client.search(prompt)
    print(results)

if __name__ == "__main__":
    main()

'''
