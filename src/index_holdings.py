import pandas as pd


def index_holdings(file):
    with open(file, "r") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if line.startswith("Ticker"):
            header_row = i
        if line.strip() == '""':
            footer_row = len(lines) - i
            break
        
    
    holdings = pd.read_csv(file, skiprows=header_row, skipfooter=footer_row, engine='python')
    
    return holdings


