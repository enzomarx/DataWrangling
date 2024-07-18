import pdfplumber

def extract_table_to_csv(pdf_path, output_csv_path):
    """Extracts table data from a PDF and saves it as a CSV file."""
    with pdfplumber.open(pdf_path) as pdf:
        # Assuming the table is on the first page
        page = pdf.pages[0]
        
        # Extract tables from the page
        tables = page.extract_tables()

        if tables:
            # Assuming we want to extract the first table 
            table_data = tables[0] 

            # Convert table data to CSV format
            csv_data = "\n".join([",".join(map(str, row)) for row in table_data])

            # Save CSV data to file
            with open(output_csv_path, "w", encoding="utf-8") as f:
                f.write(csv_data)
            print(f"Table data extracted to: {output_csv_path}")
        else:
            print("No tables found on the page.")

# Replace with your actual PDF file path and desired output CSV file path
pdf_file_path = "arq.PDF"
output_csv_path = "extracted_table_data.csv"

extract_table_to_csv(pdf_file_path, output_csv_path)