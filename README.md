# 🏠 Hostel & Flat Expense Manager

A Python-based desktop application for calculating and sharing hostel and flat expenses. The application provides a modern dark-mode graphical interface, automatic bill calculations, per-person expense sharing, and PDF receipt generation.

## 📌 Project Overview

The **Hostel & Flat Expense Manager** simplifies the calculation of shared living expenses, including monthly rent, food costs, and electricity bills.

Users can enter their expenses, select the number of people sharing the bill, view the total amount and individual contributions, and download a detailed PDF receipt.

This project was developed using Python with a focus on a simple, user-friendly desktop interface.

## ✨ Features

- **Expense Calculation:** Calculate rent, food, and electricity expenses.
- **Electricity Bill Calculation:** Calculate electricity costs using units consumed and the rate per unit.
- **Expense Sharing:** Divide the total bill among 2, 4, 6, 8, or 10 people.
- **Dashboard Summary:** Display the total bill and per-person amount.
- **PDF Receipt Generation:** Generate and save detailed expense receipts.
- **Automatic Bill Number:** Generate a bill number based on the current date and time.
- **Input Validation:** Handle invalid numeric inputs and negative expenses.
- **Reset Functionality:** Clear the form to start a new calculation.
- **Modern Dark Interface:** A dark-themed GUI built with CustomTkinter.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **CustomTkinter** — Modern graphical user interface
- **Tkinter** — File dialogs and message boxes
- **ReportLab** — PDF receipt generation
- **Datetime** — Date and time handling

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your computer
- pip package installer

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd hostel-flat-expense-manager
```

### Step 3: Install Dependencies

```bash
pip install customtkinter reportlab
```

### Step 4: Run the Application

```bash
python expense_manager.py
```

## 📖 How to Use

1. Enter the monthly rent.
2. Enter the total food expenses.
3. Enter the electricity units consumed.
4. Enter the electricity charge per unit.
5. Select the number of people sharing the expenses.
6. Click **Calculate Expenses** to calculate and display the bill.
7. Review the total bill and per-person amount.
8. Click **Download PDF** to save the expense receipt.
9. Click **Reset Form** to clear the current entries.

## 🧮 Calculation Logic

The application uses the following formulas:

- **Electricity Bill** = Electricity Units × Charge Per Unit
- **Total Bill** = Rent + Food Expenses + Electricity Bill
- **Per-Person Amount** = Total Bill ÷ Number of Persons

## 📂 Project Structure

```text
hostel-flat-expense-manager/
│
├── expense_manager.py
├── README.md
├── requirements.txt
└── screenshots/
    ├── main-application.png
    ├── expense-calculation.png
    └── pdf-receipt.png
```

## 🚀 Future Improvements

- Add a database to store and retrieve previous bills.
- Implement expense history and monthly reports.
- Add customizable expense categories.
- Support Excel export.
- Improve input validation and reporting features.

## 👩‍💻 Developer

**Fatima Mughal**

- **GitHub:** [@fatimamughal12](https://github.com/fatimamughal12)
- **LinkedIn:** [Fatima Mughal](https://www.linkedin.com/in/fatima-mughal-b99780372/)

## 📄 License

This project is intended for educational and portfolio purposes. A formal open-source license can be added if the project is published for public reuse and distribution.
