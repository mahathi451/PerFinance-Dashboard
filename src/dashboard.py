import streamlit as st
from data_processor import FinanceData
from config import DEFAULT_CURRENCY

# Initialize dashboard
st.set_page_config(layout="wide")
st.title(f"Personal Finance Dashboard ({DEFAULT_CURRENCY})")

@st.cache_resource
def load_finance_data():
    try:
        return FinanceData()
    except ValueError as e:
        st.error(str(e))
        st.stop()

finance_data = load_finance_data()

# Main layout
col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(finance_data.plot_budget_status(), use_container_width=True)

with col2:
    budget_status = finance_data.get_budget_status()
    st.metric("Total Spending", 
             f"{budget_status['Amount'].sum():.2f}",
             delta=f"{budget_status['Remaining'].sum():.2f} Remaining")
