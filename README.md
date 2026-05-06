# Finance-App

A lightweight desktop application for managing and documenting your income, expenses, and financial records with an intuitive graphical interface.

**Version:** 1.5  
**Author:** Ryan Bodner  
**License:** © 2026 Ryan Bodner

---

## 🎯 Overview

Finance-App is a user-friendly desktop application built with Python and Tkinter that helps you track your financial transactions. Easily log profits and expenses, manage your data, and gain insights into your financial patterns with built-in features like savings percentage tracking.

## ✨ Features

- **Transaction Logging** — Record income and expenses in an organized manner
- **Data Persistence** — Save and load your financial records
- **Savings Tracking** — Monitor your savings percentage with customizable thresholds
- **User-Friendly Interface** — Clean, intuitive Tkinter-based GUI
- **Secure Exit** — Prompt to save data before closing the application

## 📋 Requirements

- **Python 3.7+**
- **tkinter** (usually included with Python)
- **Babel** (for internationalization support)

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Yummypieisyummy/Finance-App.git
cd Finance-App
```

### Running the Application

**From Source:**
```bash
cd src/components
python main.py
```

**From Compiled Binary:**
Navigate to `src/components/build/main/` and run the `main.exe` executable.

## ⚙️ Configuration

The application uses a `config.json` file for settings:

```json
{
  "savings_percentage": 50.0,
  "window_width": 1200,
  "window_height": 700
}
```

**Configuration Options:**
- `savings_percentage` — Target percentage of income to save (default: 50%)
- `window_width` — Application window width in pixels (default: 1200)
- `window_height` — Application window height in pixels (default: 700)

Edit these values to customize the application behavior.

## 📁 Project Structure

```
Finance-App/
├── config.json              # Application configuration
├── README.md               # This file
├── src/
│   └── components/
│       ├── main.py         # Application entry point
│       ├── interface.py    # GUI components
│       ├── dataStorage.py  # Data persistence logic
│       ├── commands.py     # Command handlers
│       ├── itemClass.py    # Transaction item class
│       └── main.spec       # PyInstaller build configuration
```

## 📖 Usage

1. Launch the application
2. Enter transaction details (amount, description, type)
3. View your transaction history and financial summary
4. Adjust settings in `config.json` as needed
5. Exit the application (you'll be prompted to save changes)

## 🔧 Development

**Main Components:**
- `main.py` — Application initialization and window management
- `interface.py` — Tkinter GUI layout and user interactions
- `dataStorage.py` — Configuration loading and transaction persistence
- `commands.py` — Business logic for transaction handling
- `itemClass.py` — Data model for individual transactions

## 📝 License

Copyright © 2026 Ryan Bodner

---

**Last Updated:** May 2026
