# 📊 Personal Finance Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458)

A dynamic web application for personal financial management and budget analysis.

## 🚀 Key Features

### 📈 Data Visualization
- Interactive line charts for spending trends
- Pie charts for category breakdowns
- Budget vs actual comparison bars
- Real-time updates on data changes

### 🔧 Core Functionality
- CSV/Excel file upload with validation
- Customizable budget limits per category
- Multi-currency support (USD, EUR, GBP)
- Automated monthly reports generation

## 🛠 Technical Stack

**Frontend**  
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit)  
**Backend**  
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas)  
![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly)  

## ⚙ Installation

Clone repository

git clone https://github.com/yourusername/finance-dashboard.git
Create virtual environment

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
text

## 🖥 Usage

1. Prepare your data files:
   - `data/transactions.csv` (required columns: Date, Description, Amount, Category)
   - `data/categories.csv` (required columns: Category, Type)

2. Launch application:
streamlit run src/dashboard.py
text

3. Access dashboard at `http://localhost:8501`

## ⚙ Configuration

Modify `src/config.py`:
Currency settings

DEFAULT_CURRENCY = "USD" # Change to EUR/GBP
Budget limits

BUDGET_LIMITS = {
"Essential": 2500.00,
"Luxury": 800.00
}
Chart styling

CHART_STYLE = {
"width": 1200,
"height": 600,
"template": "plotly_dark"
}
text

## 📸 Screenshots

![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Finance+Dashboard+Interface)

## 📜 License
MIT License - See [LICENSE](LICENSE) for details
