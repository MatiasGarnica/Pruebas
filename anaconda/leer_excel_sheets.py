import pandas as pd

def leer_sheet_publica(sheet_id, sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid={sheet_name}"
    df = pd.read_excel(url)
    print(df.head())



sheet_id = "1mhG8jFs6kjUBVBTFTi9hVgosW7cSqs0I"
sheet_name = "personas"
leer_sheet_publica(sheet_id, sheet_name)