import pandas as pd
import plotly.express as px
from config import DATA_DIR, CHART_STYLE, BUDGET_LIMITS
from utils import validate_transaction_data

class FinanceData:
    def __init__(self):
        self.transactions = self._load_transactions()
        self.categories = pd.read_csv(DATA_DIR / 'categories.csv')
        
    def _load_transactions(self):
        df = pd.read_csv(DATA_DIR / 'transactions.csv', parse_dates=['Date'])
        if not validate_transaction_data(df):
            raise ValueError("Invalid transaction data format")
        return df
        
    def get_budget_status(self):
        merged = pd.merge(self.transactions, self.categories, on='Category')
        spending = merged.groupby('Type')['Amount'].sum().reset_index()
        spending['Budget'] = spending['Type'].map(BUDGET_LIMITS)
        spending['Remaining'] = spending['Budget'] - spending['Amount']
        return spending

    def plot_budget_status(self):
        status = self.get_budget_status()
        fig = px.bar(status, 
                    x='Type', y=['Amount', 'Budget'],
                    barmode='group',
                    title="Budget vs Actual Spending",
                    **CHART_STYLE)
        return fig
