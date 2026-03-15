import requests
import pandas as pd
from datetime import datetime

def extract(country):
    """Fetch raw data from the public Universities API."""
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def transform(raw_data):
    """Clean and structure the data using Pandas."""
    df = pd.DataFrame(raw_data)
    
    # 1. Select and rename relevant columns
    df = df[['name', 'country', 'state-province', 'web_pages']]
    df.columns = ['University_Name', 'Country', 'State_Province', 'Website']
    
    # 2. Handle missing values in State/Province
    df['State_Province'] = df['State_Province'].fillna('Unknown')
    
    # 3. Clean 'Website' column (extract first URL from list)
    df['Website'] = df['Website'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else "")
    
    # 4. Add a metadata column for when the record was processed
    df['processed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return df

def load(df, filename="transformed_universities.csv"):
    """Save the cleaned data to a CSV file."""
    df.to_csv(filename, index=False)
    print(f"Successfully loaded {len(df)} records to {filename}")

if __name__ == "__main__":
    # Change 'Kenya' to any country to see the data shift!
    target_country = "Kenya"
    
    print(f"Starting ETL for: {target_country}...")
    raw = extract(target_country)
    
    if raw:
        clean_df = transform(raw)
        load(clean_df)
        print("Pipeline execution complete.")