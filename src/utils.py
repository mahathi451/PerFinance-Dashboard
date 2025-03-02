from datetime import datetime
import pandas as pd

def validate_transaction_data(df: pd.DataFrame) -> bool:
    required_columns = {'Date', 'Description', 'Amount', 'Category'}
    if not required_columns.issubset(df.columns):
        return False
    if df['Amount'].min() < 0:
        return False
    try:
        pd.to_datetime(df['Date'])
    except:
        return False
    return True
