# Binance Futures Order CLI

A robust Python command-line interface (CLI) for executing trades on the Binance Futures Testnet. Built with strict input validation, logging, and error handling.

---

## ✨ Features

- **Order Types Supported:** Place `MARKET`, `LIMIT`, and `STOP_LIMIT` orders.
- **Input Validation:** Automatically validates trading pair symbols, side (`BUY`/`SELL`), quantity, and price formats before sending requests.
- **Logging System:** Logs API responses, order details, and execution errors to log files for tracking.
- **Testnet Ready:** Safely test strategies using Binance Futures Testnet credentials without risking real capital.

---

## 🛠️ Project Structure

```text
binance_order_cli/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── cli.py
├── requirements.txt
└── .env.example
---
---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aaryajogdand/binance_order_cli.git](https://github.com/aaryajogdand/binance_order_cli.git)
