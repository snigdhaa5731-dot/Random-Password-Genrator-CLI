# 🔐 Random Password Generator CLI

A lightweight, interactive command-line password generator built with Python. It generates customizable passwords based on user-selected character categories and configurable complexity requirements.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Standard Library](https://img.shields.io/badge/Dependencies-None-success.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Execution](#-sample-execution)
- [Password Generation Logic](#-password-generation-logic)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

The **Random Password Generator CLI** is a standalone Python application designed to simplify password generation through an interactive terminal interface.

Users can specify their desired password length and select which character categories should be included.

The generator enforces basic complexity rules and ensures that every selected character category is represented in the generated password.

Its lightweight implementation uses Python's standard library, eliminating the need for third-party dependencies.

---

## ✨ Key Features

### 🔒 Password Complexity Enforcement

- Minimum password length of 8 characters.
- Requires at least two distinct character categories.
- Supports customizable character combinations.
- Validates user inputs before generating passwords.

### 🔤 Customizable Character Sets

Users can select from four character categories:

| Category | Characters |
|---|---|
| Uppercase | `A-Z` |
| Lowercase | `a-z` |
| Numbers | `0-9` |
| Special Symbols | `!@#$%...` |

### ⚡ Intelligent Generation

- Guarantees at least one character from every selected category.
- Combines selected character sets.
- Randomizes the final character sequence.
- Supports repeated password generation within a single session.

### 🖥️ Interactive CLI

- Simple terminal-based interface.
- Step-by-step user input.
- Password length customization.
- Continuous generation until the user exits.

### 📦 Zero External Dependencies

Built using Python standard library modules:

- `random`
- `string`
- `sys`

No external package installation is required.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| random | Randomized selection and shuffling |
| string | Character set definitions |
| sys | Command-line and application utilities |

---

## 💻 Prerequisites

Requirements:

- Python 3.10 or higher
- Terminal / Command Prompt
- Git (optional)

Verify Python installation:

```bash
python --version
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/LAKSHYAMARODIA01/python-projects.git
cd python-projects/password-generator
```

### 2. Run the Application

```bash
python password_generator.py
```

That's it!

No virtual environment or external dependencies are required for this standalone application.

---

## 🎮 Usage

When the program starts, it asks the user to configure password generation.

### Configuration Steps

1. Enter the desired password length.
2. Choose whether to include uppercase letters.
3. Choose whether to include lowercase letters.
4. Choose whether to include numbers.
5. Choose whether to include special symbols.
6. Generate the password.
7. Choose whether to generate another password or exit.

---

## 🖥️ Sample Execution

```text
==================================================
             RANDOM PASSWORD GENERATOR
==================================================

Enter total password length (min: 8): 14

Include Uppercase letters? (y/n): y
Include Lowercase letters? (y/n): y
Include Numbers? (y/n): y
Include Special Symbols? (y/n): y

--------------------------------------------------
Generated Password:
  >>> k(cYwv8N|+VF9Q <<<
Length: 14 characters
--------------------------------------------------

Generate another password? (y/n): n
```

*Note: The generated password will be different on each execution.*

---

## 🧠 Password Generation Logic

The application follows a structured generation process:

1. **Input Validation:** Checks the requested password length and character category selections.
2. **Character Selection:** Builds character pools based on the user's preferences.
3. **Category Representation:** Selects at least one character from every enabled category.
4. **Password Completion:** Fills the remaining positions using the combined character pool.
5. **Randomization:** Shuffles the generated characters.
6. **Output:** Displays the resulting password and its length.

### Complexity Rules

| Rule | Requirement |
|---|---|
| Minimum Length | 8 characters |
| Character Categories | Minimum 2 |
| Uppercase | Optional |
| Lowercase | Optional |
| Numbers | Optional |
| Special Symbols | Optional |
| Repeated Generation | Supported |

**Security Note:** The current implementation uses Python's `random` module. For passwords protecting sensitive accounts, replace it with Python's `secrets` module and its cryptographically secure selection and shuffling methods.

---

## 📂 Project Structure

```text
password-generator/
│
├── password_generator.py    # Main password generator
└── README.md                 # Project documentation
```

---

## 🛠️ Troubleshooting

| Problem | Recommended Solution |
|---|---|
| Python not recognized | Add Python to PATH or use `py` / `python3` |
| Invalid password length | Enter a number greater than or equal to 8 |
| Insufficient character categories | Select at least two character categories |
| Application exits unexpectedly | Check the entered values and restart the script |

---

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m "feat: improve password generation"
   ```

4. Push your branch:

   ```bash
   git push origin feature/AmazingFeature
   ```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software in accordance with the license conditions.

---

**Built with Python 🐍**
