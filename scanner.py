import requests
from bs4 import BeautifulSoup
import json

def scan_website(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all('script', src=True)
    return [script['src'] for script in scripts]

def detect_trackers(script_urls):
    with open("tracker_list.json") as f:
        tracker_db = json.load(f)

    found = []
    for url in script_urls:
        for tracker in tracker_db:
            if tracker in url:
                found.append((tracker, tracker_db[tracker]))
    return found

def calculate_risk(tracker_count):
    if tracker_count == 0:
        return "Very Low Risk"
    elif tracker_count <= 2:
        return "Low Risk"
    elif tracker_count <= 5:
        return "Medium Risk"
    else:
        return "High Risk"
