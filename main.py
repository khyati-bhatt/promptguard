import argparse
from detector import Detector
from url_scanner import fetch_url
import json
from url_scanner import active_scan

def main():
    parser = argparse.ArgumentParser(
        description="Prompt Guard - AI Security Scanner"
    )

    parser.add_argument("-t", "--text", help="Scan raw input text")
    parser.add_argument("-f", "--file", help="Scan file content")
    parser.add_argument("-u", "--url", help="Target URL to scan")

    parser.add_argument("--method", default="GET", help="HTTP method (GET/POST)")
    parser.add_argument("--data", help="JSON request body")
    parser.add_argument("--headers", help="JSON headers")

    parser.add_argument("--active", action="store_true", help="Enable active attack mode")

    args = parser.parse_args()
    detector = Detector()

    data = None

    if args.active and not args.data:
        print("[-] Active mode requires --data")
        return
    if args.text:
        data = args.text

    elif args.file:
        with open(args.file, "r") as f:
            data = f.read()

    elif args.url and args.active:
        with open("payloads.json", "r") as f:
            payloads = json.load(f)["prompt_injection"]

        active_scan(
            args.url,
            args.method,
            args.headers,
            args.data,
            payloads
        )
        return
    
    elif args.url:
        data = fetch_url(args.url)

    else:
        print("Provide --text, --file, or --url")
        return

    findings = detector.scan(data)

    if not findings:
        print("[+] No issues found")
        return

    risk = detector.score(findings)

    print(f"\n[!] Risk Level: {risk}\n")

    for f in findings:
        if f["type"] == "entropy":
            print(f"[ENTROPY] {f['value']} (H={f['entropy']})")
        else:
            print(f"[PATTERN] {f['severity'].upper()} -> {f['value']}")

if __name__ == "__main__":
    main()