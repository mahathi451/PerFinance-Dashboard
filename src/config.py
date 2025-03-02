import pathlib

# Path configuration
BASE_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Financial parameters
DEFAULT_CURRENCY = "USD"
BUDGET_LIMITS = {
    "Essential": 2000.00,
    "Luxury": 500.00
}

# Visualization settings
CHART_STYLE = {
    "width": 800,
    "height": 400,
    "template": "plotly_white"
}
