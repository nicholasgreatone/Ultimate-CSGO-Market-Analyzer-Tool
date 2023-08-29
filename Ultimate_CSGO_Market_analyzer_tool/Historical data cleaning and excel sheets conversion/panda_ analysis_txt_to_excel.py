import pandas as pd
import re

# Read the text file
text_file_path = "output.txt"
with open(text_file_path, 'r') as f:
    text_data = f.read()

# Split the text data into cases
cases = re.split(r'\n\n', text_data)

# Create an empty DataFrame
data = {
    'Case': [],
    'Year': [],
    'Month': [],
    'Average Price': []
}
df = pd.DataFrame(data)

# Process each case and extract data
for case in cases:
    lines = case.strip().split('\n')
    case_name = lines[0]
    year_lines = lines[1:]
    
    for year_line in year_lines:
        year_match = re.match(r'Year: (\d{4})', year_line)
        if year_match:
            year = year_match.group(1)
        
        month_matches = re.findall(r'(\w+): Average Price = \$([\d.]+)', year_line)
        for month, avg_price in month_matches:
            df = df.append({
                'Case': case_name,
                'Year': year,
                'Month': month,
                'Average Price': avg_price
            }, ignore_index=True)

# Write to Excel file
excel_file_path = "csgo_case_USD_history.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Text file converted to Excel: {excel_file_path}")
