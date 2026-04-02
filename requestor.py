import requests
import json

def send_request(url, method="GET", headers=None, data=None, timeout=5):
    try:
        if headers:
            headers = json.loads(headers)

        if data:
            data = json.loads(data)

        if method.upper() == "POST":
            res = requests.post(url, json=data, headers=headers, timeout=timeout)
        else:
            res = requests.get(url, headers=headers, timeout=timeout)

        return res.text

    except Exception as e:
        return f"ERROR: {str(e)}"