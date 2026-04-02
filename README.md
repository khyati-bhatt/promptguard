# Prompt Guard 🔐

🚀 A lightweight CLI tool to actively test AI systems for **prompt injection attacks** and **sensitive data leaks**.

---

## 📌 Version

Current: **v2.0.0**

---

## 🚀 Features

* 🧠 Prompt injection detection (pattern-based)
* 🔐 Entropy-based secret detection (API keys, tokens)
* 🌐 Passive URL scanning
* 💣 Active attack mode (payload injection)
* 🔁 Response comparison (reflection + behavior change)
* ⚡ Simple and fast CLI interface

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

---

### 🔹 Scan file

```bash
python main.py -f sample.txt
```

---

### 🔹 Passive URL scan

```bash
python main.py -u https://example.com
```

---

### 🔥 Active Scan (v2)

```bash
python main.py -u http://localhost:5000/chat \
--method POST \
--headers '{"Content-Type":"application/json"}' \
--data '{"message":"hello"}' \
--active
```

### What it does:

* Sends baseline request
* Injects prompt payloads
* Compares responses
* Detects leaks, reflections, anomalies

---

## 📊 Example Output

```
[ACTIVE SCAN] http://localhost:5000/chat

▶ Payload: ignore previous instructions
  ↳ Response Changed: YES
  ↳ Reflection: NO
  ↳ Risk: HIGH
  ↳ Findings:
     - LEAK: system prompt
     - LEAK: secret

--------------------------------------------------
```

---

## 🧠 Detection Capabilities

### 1. Prompt Injection Detection

Detects malicious instructions such as:

* ignore previous instructions
* reveal system prompt
* bypass safety filters

---

### 2. Entropy-Based Secret Detection

Identifies high-entropy strings like:

* API keys (`sk-...`)
* tokens
* encoded secrets

---

### 3. Sensitive Data Leak Detection

Flags exposure of:

* system prompts
* secrets
* configuration data

---

## 🏗️ Architecture

```
            INPUT
   (text / file / URL)
           ↓
     Request Engine
           ↓
   Payload Injection (optional)
           ↓
       Response
           ↓
   Detection Engine
   ├── Pattern Matching
   ├── Entropy Analysis
   └── Leak Detection
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
 ├── requestor.py
 ├── injector.py
 ├── comparer.py
 ├── payloads.json
 ├── patterns.json
 └── README.md
```

---

## 🛡️ Use Cases

* Bug bounty testing for AI/LLM endpoints
* Prompt injection vulnerability analysis
* API response auditing
* AI security research

---

## ⚠️ Limitations

* Single-field injection (`message` only)
* No async scanning
* Limited payload set

---

## 🚀 Roadmap

* [ ] Multi-field injection
* [ ] Advanced response diffing
* [ ] Burp Suite integration
* [ ] Web UI dashboard

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

MIT License
