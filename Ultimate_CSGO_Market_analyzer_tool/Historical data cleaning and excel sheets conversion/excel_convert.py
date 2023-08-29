import pandas as pd

print("Starting file creation! :)")

text_file_path = "C:\SQL\case_data\output.txt"
combined_data = []

with open(text_file_path, 'r') as f:
    current_case = ""
    current_year = ""

    for line in f:
        line = line.strip()
        if line:
            if line.endswith("Case:"):
                current_case = line
            elif line.startswith("Year:"):
                current_year = line.split(" ")[1]
            else:
                month, avg_price = line.split(":")[0].strip(), line.split(":")[1].strip()
                combined_data.append((current_case, current_year, month, avg_price))

data = {
    'Case': [item[0] for item in combined_data],
    'Year': [item[1] for item in combined_data],
    'Month': [item[2] for item in combined_data],
    'Average Price': [item[3] for item in combined_data]
}

df = pd.DataFrame(data)
excel_file_path = "csgo_case_USD_history.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Text file converted to Excel: {excel_file_path}")



