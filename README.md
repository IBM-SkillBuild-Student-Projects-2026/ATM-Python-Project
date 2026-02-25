# 🏧 ATM Simulation Program

A simple Python-based ATM simulation that allows users to perform basic banking operations through a command-line interface.

---

## ✨ Features

* 💰 **Check Balance** – View your current account balance
* ➕ **Deposit Funds** – Add money to your account
* ➖ **Withdraw Cash** – Withdraw money with insufficient fund protection
* 🚪 **Exit** – Safely exit the ATM system

---

## ⚙️ How It Works

The program runs inside an infinite loop displaying an ATM menu with four options:

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Users select an option by entering the corresponding number.
The program validates inputs and provides appropriate feedback for each transaction.

---

## ▶️ Usage

1. Run the Python script:

```bash
python ATM.py
```

2. Select an option from the menu by entering **1–4**
3. Follow the prompts for deposits and withdrawals
4. Choose option **4** to exit the program

---

## 🖥 Sample Interaction

```
--- ATM MENU ---
1. Check your Balance
2. Deposit
3. Withdraw
4. Exit

Enter your choice : 1
Your Balance is: 1000
```

---

## 🛠 Requirements

* Python 3.x
* No additional libraries required

---

## 🧠 Code Structure

* `balance` → Initial account balance (set to 1000)
* `while True` loop → Keeps ATM running continuously
* Conditional statements (`if-elif-else`) → Handle menu options
* Withdrawal validation → Prevents insufficient balance transactions

---

## 👩‍💻 Author

**Vicky**
IBM SkillBuild 2026 Batch
