# 🔐 Password Strength Tester

A lightweight command-line tool for analysing password strength using the battle-tested [zxcvbn](https://github.com/dropbox/zxcvbn) library. Works in two modes: **interactive** (type one password) or **batch** (analyse a whole file of passwords at once).

---

## Features

- Scores each password from **0 (very weak) to 4 (very strong)**
- Reports **estimated crack time** under a realistic offline attack scenario
- Provides **human-readable improvement suggestions**
- Supports **batch processing** — point it at a wordlist and get a report for every entry
- Password input is **hidden from the terminal** in interactive mode (via `getpass`)

---

## Requirements

- Python 3.7+
- [zxcvbn](https://pypi.org/project/zxcvbn/) library

Install the dependency:

```bash
pip install zxcvbn
```

---

## Usage

### Interactive mode — single password

```bash
python test_password_strength.py
```

You will be prompted to enter a password. Input is hidden as you type.

**Example output:**

```
[?] Enter your password:
Value:      hunter2
Score:      1/4
Crack Time: 3 minutes
Feedback:   ['Add another word or two. Uncommon words are better.']
```

---

### Batch mode — analyse a file of passwords

```bash
python test_password_strength.py passwords.txt
```

The file should contain one password per line. Each password gets its own report block.

**Example `passwords.txt`:**

```
hunter2
correct-horse-battery-staple
P@ssw0rd!
```

**Example output:**

```
[+] ######################
Value:      hunter2
Score:      1/4
Crack Time: 3 minutes
Feedback:   ['Add another word or two. Uncommon words are better.']

[+] ######################
Value:      correct-horse-battery-staple
Score:      4/4
Crack Time: centuries
Feedback:   []
```

---

## Score Reference

| Score | Meaning         |
|-------|-----------------|
| 0     | Very weak       |
| 1     | Weak            |
| 2     | Fair            |
| 3     | Strong          |
| 4     | Very strong     |

The crack time shown is estimated for an **offline slow-hash attack at 10,000 guesses/second** — a realistic scenario for a stolen hashed password database.

---

## Project Structure

```
.
├── test_password_strength.py   # Main script
└── passwords.txt               # (Optional) sample password list for batch mode
```
