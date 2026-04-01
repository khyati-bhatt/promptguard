import requests

def fetch_url(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"ERROR: {str(e)}"