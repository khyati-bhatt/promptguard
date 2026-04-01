import argparse
from detector import Detector
from url_scanner import fetch_url

def main():
    parser = argparse.ArgumentParser(description="Prompt Guard Pro")
    parser.add_argument("-t", "--text", help="Scan raw text")
    parser.add_argument("-f", "--file", help="Scan file")
    parser.add_argument("-u", "--url", help="Scan URL (passive)")

    args = parser.parse_args()
    detector = Detector()

    data = None

    if args.text:
        data = args.text

    elif args.file:
        with open(args.file, "r") as f:
            data = f.read()

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