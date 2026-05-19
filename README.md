# 🤖 Simple Chatbot

A lightweight, rule-based command-line chatbot written in Python. Designed as a beginner-friendly project to demonstrate basic conversational logic using conditional statements.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Supported Commands](#supported-commands)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Simple Chatbot is a Python terminal application that responds to a fixed set of user inputs. It runs in an interactive loop, reads user messages, and returns predefined responses — making it an ideal starting point for understanding chatbot fundamentals.

---

## Features

- ✅ Interactive command-line interface
- ✅ Case-insensitive input handling
- ✅ Clean and readable code structure
- ✅ Graceful exit on `bye` command
- ✅ Zero external dependencies

---

## Getting Started

### Prerequisites

- Python **3.x** installed on your machine
- A terminal or command prompt

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/simple-chatbot.git
   cd simple-chatbot
   ```

2. **No additional packages required** — the project uses only the Python standard library.

### Usage

Run the chatbot with:

```bash
python Simple_Chat_Bot.py
```

**Example session:**

```
Chatbot Started!
Type 'bye' to exit.

You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

---

## Supported Commands

| User Input     | Bot Response              |
|----------------|---------------------------|
| `hello`        | Hi!                       |
| `how are you`  | I'm fine, thanks!         |
| `name`         | I am a basic chatbot.     |
| `bye`          | Goodbye! *(exits)*        |
| *(anything else)* | Sorry, I don't understand. |

> Input is **case-insensitive** — `Hello`, `HELLO`, and `hello` all work the same.

---

## Project Structure

```
simple-chatbot/
│
├── Simple_Chat_Bot.py   # Main chatbot script
└── README.md            # Project documentation
```

---

## Future Improvements

- [ ] Add more conversational responses
- [ ] Integrate NLP for natural language understanding
- [ ] Build a web or GUI interface
- [ ] Store conversation history to a log file
- [ ] Add multi-language support

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ in Python</p>
