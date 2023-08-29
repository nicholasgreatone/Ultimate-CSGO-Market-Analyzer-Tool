
#Nicholas Odeh, aka Altoids.exe, Nicholasgreatone
#imports used for program
import datetime  #helps format date data for outputs Essential_Import_Used_for_Processing_Dates_pulls_the_months_and_days_for_USD_average_month_value
import json  # Essential_import___Used_for_reading_json_data
import os  # Essential_import___Used_for_locating_the___case_data___file
import colorama  # for_aesthetics_delete_colorama_and_associated_code_if_not_wanted
colorama.init()  # inits_the_colorama_package

# Set the path to the folder containing case data
path = "case_data"
file_list = os.listdir(path)

# Display case names found
print(f'\n {colorama.Fore.GREEN} \t   * Files found *{colorama.Style.RESET_ALL}')
print(f' {colorama.Fore.GREEN} \t * Case Names Found *{colorama.Style.RESET_ALL} \n')
print(f'{colorama.Fore.RED}  *Case Names*{colorama.Style.RESET_ALL}')

# Clean up file names for display
cleaned_filenames = [filename.replace('_', ' ').replace('.json', '') for filename in file_list]
for cleaned_filename in cleaned_filenames:
    print(cleaned_filename)

# Wait for user input to start data processing
input(f' \n \t {colorama.Fore.GREEN}* Paused, press space to start data processing *{colorama.Style.RESET_ALL}')

# Open a text file for writing
output_file_path = "output.txt"
output_file = open(output_file_path, "w")

# Iterate through files and process data
for file, cleaned_filename in zip(file_list, cleaned_filenames): 
    file_path = os.path.join(path, file)
    
    # Reads JSON Files From Case Data Folder
    with open(file_path, 'r') as json_file:
        case_data = json.load(json_file)
        print(f'\nData from {colorama.Fore.MAGENTA}{cleaned_filename.title()}{colorama.Style.RESET_ALL}:')
        output_file.write(f'\n{cleaned_filename.title()}:')

        # Organize Historical USD Values By Year And Month
        data_by_year_month = {}
        for USD in case_data["prices"]:
            date_str, price, _ = USD
            date_str = date_str.replace(" +0", "")  # Remove offset
            date = datetime.datetime.strptime(date_str, "%b %d %Y %H:")  # strips junk from json if present
            year = date.year  # displays year in red
            month = date.strftime("%B")  # strips junk from json if present

            if year not in data_by_year_month:
                data_by_year_month[year] = {}

            if month not in data_by_year_month[year]:
                data_by_year_month[year][month] = []

            data_by_year_month[year][month].append(price)

        # Prints Historical USD Values By Year And Month
        for year, months in data_by_year_month.items():
            print(f' \nYear: {year}')
            output_file.write(f'\nYear: {year}\n')
            for month, prices in months.items():
                average_price = sum(prices) / len(prices)
                print(f"  {month}: Average Price = {average_price:.2f}")
                output_file.write(f"  {month}:{average_price:.2f}\n")
        
        

# Close the text file
output_file.close()
print(" ")
print(f'{colorama.Fore.MAGENTA}historical price data collection done{colorama.Style.RESET_ALL}')
print (" ")
print(f"Output saved to {colorama.Fore.MAGENTA}{output_file_path}{colorama.Style.RESET_ALL}")
