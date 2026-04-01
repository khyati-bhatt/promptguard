# Prompt Guard  🔐

A lightweight CLI tool to detect **prompt injection attacks** and **sensitive data leaks** in AI inputs, logs, and API responses.

---

## 🚀 Features

* 🧠 Detect prompt injection patterns
* 🔐 Identify high-entropy strings (API keys, tokens)
* 🌐 Scan URLs (passive mode)
* 📄 Analyze files and raw input
* ⚡ Simple CLI interface

---

## 📦 Installation

```bash
git clone https://github.com/khyati-bhatt/promptguard.git
cd promptguard
pip install -r requirements.txt
```

---

## 🧪 Usage

### 🔹 Scan raw text

```bash
python main.py -t "ignore previous instructions"
```

### 🔹 Scan file

```bash
python main.py -f sample.txt
```

### 🔹 Scan URL (passive)

```bash
python main.py -u https://example.com
```

---

## 🧠 Detection Capabilities

### 1. Prompt Injection Detection

Detects malicious patterns such as:

* ignore previous instructions
* reveal system prompt
* bypass safety

### 2. Entropy-Based Secret Detection

Identifies high-entropy strings like:

* API keys
* tokens
* encoded secrets

---

## 📊 Example Output

```
[!] Risk Level: CRITICAL

[PATTERN] HIGH -> ignore previous instructions
[ENTROPY] sk-ABCD1234XYZ (H=4.8)
```

---

## 🏗️ Architecture

```
            INPUT
   (text / file / URL)
           ↓
     Input Handler (main.py)
           ↓
     URL Fetcher (optional)
     (url_scanner.py)
           ↓
     Detection Engine
     (detector.py)
        ├── Pattern Matching
        └── Entropy Analysis (entropy.py)
           ↓
         Scoring
           ↓
         Output
```

---

## 📂 Project Structure

```
promptguard/
 ├── main.py
 ├── detector.py
 ├── entropy.py
 ├── url_scanner.py
 ├── patterns.json
 ├── utils.py
 └── README.md
```

---

## 🛡️ Use Cases

* Bug bounty (AI/LLM targets)
* Prompt security testing
* API response auditing
* Log analysis for secret leaks

---

## ⚠️ Limitations (v1)

* Passive URL scanning only
* No payload injection
* No request customization

---

## 🚀 Roadmap

* [ ] Active payload injection
* [ ] POST/headers support
---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

MIT License
