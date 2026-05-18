<h1 align="center">🔒 v2 - Pwned Password Check</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue">
  <img src="https://img.shields.io/badge/API-Have%20I%20Been%20Pwned-orange">
</p>

<p align="center"><b>Upgraded version that checks if your password has been exposed in data breaches using the Have I Been Pwned API.</b></p>

---

#### ✨ Features in v2:
- *Breach Check*: Checks your password against 600M+ compromised passwords using k-anonymity
- *Safe Hashing*: Only sends first 5 characters of SHA-1 hash to API - your password never leaves your PC
- *Strength Analysis*: Combines v1 checks - length, uppercase, symbols, common patterns
- *Detailed Feedback*: Shows how many times password was found in breaches
- *CLI Interface*: Simple command line tool, no GUI needed

---

#### ▶️ How to Run:
```bash
pip install requests
python pwned_checker.py
```
---

#### 📌 Location:
[Open v2 Folder](./password-strength-checker/v2)

---

#### 🔐 How It Works:
1. Password is converted to SHA-1 hash locally on your PC
2. First 5 characters sent to Have I Been Pwned API
3. API returns list of matching hashes
4. Script checks locally if your full hash exists
5. Your full password or full hash never leaves your computer

---
