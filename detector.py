import json
import re
from entropy import find_high_entropy_strings

class Detector:
    def __init__(self, pattern_file="patterns.json"):
        with open(pattern_file, "r") as f:
            self.patterns = json.load(f)

    def detect_patterns(self, text):
        findings = []

        for severity, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    findings.append({
                        "type": "pattern",
                        "value": pattern,
                        "severity": severity
                    })

        return findings

    def detect_entropy(self, text):
        entropy_hits = find_high_entropy_strings(text)

        results = []
        for hit in entropy_hits:
            results.append({
                "type": "entropy",
                "value": hit["value"],
                "entropy": hit["entropy"],
                "severity": "high"
            })

        return results

    def detect_sensitive_leak(self, text):
        keywords = [
            "system prompt",
            "secret",
            "config",
            "api key",
            "token"
        ]

        findings = []

        for k in keywords:
            if k in text.lower():
                findings.append({
                    "type": "leak",
                    "value": k,
                    "severity": "high"
                })

        return findings

    def scan(self, text):
        findings = []
        findings += self.detect_patterns(text)
        findings += self.detect_entropy(text)
        findings += self.detect_sensitive_leak(text)
        return findings

    def score(self, findings):
        score = 0

        for f in findings:
            if f["severity"] == "high":
                score += 3
            elif f["severity"] == "medium":
                score += 2
            else:
                score += 1

        if score >= 6:
            return "CRITICAL"
        elif score >= 4:
            return "HIGH"
        elif score >= 2:
            return "MEDIUM"
        else:
            return "LOW"