# 🛒 E-Commerce Analytics & GenAI Insight Narrator

> **From Raw Data → SQL Analytics → Python EDA → Business Insights → GenAI Narrative**

An end-to-end **E-Commerce Analytics** project that transforms raw transaction data into meaningful business insights using **MySQL Workbench, Python/Pandas, data visualization, and Google Gemini**.

---

## 🚀 Tech Stack

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge)

---

## 📂 Project Structure

```text
<repo>/
├── README.md
├── sql/
│   ├── schema.sql
│   ├── seed_data.sql
│   └── reports.sql
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
├── analysis/
│   ├── clean_and_eda.py
│   └── visualize.py
├── visualizations/
│   ├── return_rate_by_payment.png
│   └── monthly_revenue_trend.png
└── narrator/
    ├── findings.json
    └── generate_narrative.py
```

---

## 🗄️ 1. SQL Analytics — MySQL Workbench

Open **MySQL Workbench**, connect to your MySQL server, and execute the SQL files **in this exact order**:

```text
schema.sql
    ↓
seed_data.sql
    ↓
reports.sql
```

### Run:

1. Open and execute `sql/schema.sql` to create the database tables.
2. Execute `sql/seed_data.sql` to load customers, products, and orders.
3. Execute `sql/reports.sql` to generate the required business reports.

---

## 🐍 2. Python EDA & Visualization

Run the cleaning and analysis pipeline:

```bash
python analysis/clean_and_eda.py
```

This performs **data cleaning, duplicate detection, missing-value treatment, revenue reconciliation, outlier detection, return-rate analysis, correlation analysis, and monthly revenue analysis**.

> 📌 **Task 5 of Part 2 generates `narrator/findings.json`.**

Then create the visualizations:

```bash
python analysis/visualize.py
```

Generated charts:

- 📊 `return_rate_by_payment.png`
- 📈 `monthly_revenue_trend.png`

---

## 🤖 3. GenAI Insight Narrator

Run:

```bash
python narrator/generate_narrative.py
```

### 🔑 Gemini API Key

**Windows CMD:**

```bash
set GEMINI_API_KEY=your_api_key
```

**PowerShell:**

```powershell
$env:GEMINI_API_KEY="your_api_key"
```

**macOS/Linux:**

```bash
export GEMINI_API_KEY="your_api_key"
```

### 📴 No API Key?

No problem! If `GEMINI_API_KEY` is not available, the project automatically uses the **offline deterministic fallback** to generate the narrative.

---

## 🔄 Complete Workflow

```text
📦 Raw CSV Data
      ↓
🗄️ MySQL Workbench
      ↓
📊 SQL Reports
      ↓
🐍 Python Cleaning & EDA
      ↓
📄 findings.json
      ↓
📈 Visualizations
      ↓
🤖 Gemini / Offline Narrator
      ↓
💡 Executive Business Insights
```

### ⭐ Key Goal

Build a **reproducible analytics pipeline** where every business finding is generated from the underlying data and can be reproduced by following this README from top to bottom.
