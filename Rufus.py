import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class RufusforRAG:
    def __init__(self, k=None):
        self.k = k  # API Key

        chrome_opts = Options()

        # Replace with your own ChromeDriver path or make sure chromedriver.exe is in your PATH
        chrome_path = r"C:\Users\Gokul S\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe" 
        self.d = webdriver.Chrome(service=Service(chrome_path), options=chrome_opts)


    def search(self, q):
        """
        - Open Google homepage.
        - Enter query into the search bar
        - Submit the query and retrieve the search results
        - Return structured search results
        """
        print(f"Starting Google search for: {q}")
        self.d.get("https://www.google.com")

        try:
            sb = WebDriverWait(self.d, 10).until(EC.element_to_be_clickable((By.NAME, 'q')))
            sb.send_keys(q)
            sb.submit()
            print(f"Searching for '{q}' on Google.")
            time.sleep(2)
        except Exception as e:
            print(f"Error entering search term or submitting: {e}")
            self.d.quit()
            return None

        s = BeautifulSoup(self.d.page_source, 'html.parser')
        data = self.extract(s)

        self.d.quit()
        return self.structure(data)


    def extract(self, s):
        """
        - Find divs that contain search results
        - Extract the title, link, and description from each result
        - Only return results that have a non-empty description, and limit the description to 1-2 sentences
        """
        print("Extracting Google search results.")
        res = []

        for r in s.select('div#search div.g'):
            t = r.select_one('.DKV0Md').get_text() if r.select_one('.DKV0Md') else "No title"
            l = r.select_one('a')['href'] if r.select_one('a') else "No link"
            d = r.select_one('.VwiC3b').get_text() if r.select_one('.VwiC3b') else None

            if d:
                d_sentences = d.split('. ')
                d = '. '.join(d_sentences[:2]) + ('.' if len(d_sentences) > 2 else '')
                res.append({'title': t, 'link': l, 'description': d})

        return res


    def structure(self, data):
        """
        - Convert the extracted data into a structured JSON formated data
        """
        print("Structuring data into JSON format.")
        return json.dumps(data, indent=4)


    def save(self, data, f_name):
        """
        - Write the structured data to a specified JSON file
        """
        print(f"Saving structured data to {f_name}")
        with open(f_name, 'w') as f:
            json.dump(json.loads(data), f, indent=4)

def main():
    """
    - Fetch the API key from environment variables
    - Initialize RufusClient
    - Perform Google search and save the results to a JSON file
    """
    k = os.getenv('Rufus_API_KEY')  # Assume the API key is stored in an .env file
    rr = RufusforRAG(k)

    # Sample query
    q = "Currently, who is the manager of Manchester United?"

    docs = rr.search(q)
    if docs:
        print("Structured Data: \n", docs)
        rr.save(docs, 'RUFUS_results.json')
    else:
        print("No data extracted.")




if __name__ == "__main__":
    main()