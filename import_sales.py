import pandas as pd
from sqlalchemy import create_engine

csv_file_name = "retails_sales.csv" 

try:
    df = pd.read_csv(csv_file_name)
    df.columns = [c.strip().replace(' ', '_').lower() for c in df.columns]
    
    # Connecting to your database container
    engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/retail_project_db")
    
    print("Uploading data to MySQL...")
    df.to_sql("sales_data", con=engine, if_exists="replace", index=False)
    print("Success! Data successfully imported into table: sales_data")

except Exception as e:
    print(f"Error: {e}")
