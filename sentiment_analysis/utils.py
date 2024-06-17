import os
import pandas as pd

def process_files(folder_path):
    # Loop through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file is an Excel file
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            # Check if the 'HATE' column exists
            if 'HATE' in df.columns:
                # Ensure the 'HATE' column values are treated as strings
                df['HATE'] = df['HATE'].astype(str)
                
                # Create or update the 'SENTIMENT' column based on the condition
                df['SENTIMENT'] = df['HATE'].apply(lambda x: 'NEG' if pd.notna(x) and ('CAG' in x or 'OAG' in x) else None)
                
                # Save the updated DataFrame back to the Excel file
                df.to_excel(file_path, index=False)
                print(f"Processed file: {filename}")
            else:
                print(f"'HATE' column not found in file: {filename}")

# Example usage
folder_path = 'sentiment_analysis/anaïs'
process_files(folder_path)
