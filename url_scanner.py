import requests
from requestor import send_request
from injector import inject_payload
from comparer import compare_responses
from detector import Detector
import json

def active_scan(url, method, headers, data, payloads):
    detector = Detector()

    print(f"\n[ACTIVE SCAN] {url}\n")

    # baseline request
    base_response = send_request(url, method, headers, data)

    for payload in payloads:
        print(f"Payload: {payload}")

        injected_data = inject_payload(data, payload)

        injected_response = send_request(url, method, headers, injected_data)

        comparison = compare_responses(base_response, injected_response, payload)

        findings = detector.scan(injected_response)
        risk = detector.score(findings)

        if comparison["reflection"]:
            print("[!] Reflection detected")

        if comparison["length_change"]:
            print("[!] Response changed")

        if findings:
            print(f"[!] Risk: {risk}")

        print("-" * 40)

def fetch_url(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"ERROR: {str(e)}"