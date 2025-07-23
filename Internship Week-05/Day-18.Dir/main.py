import pandas as pd
import matplotlib.pyplot as plt
import os # To check if file exists

def generate_sales_report():
  
    print("--- Automated Sales Report Generator ---")

    # Bonus: Accept CSV/Excel filename from user
    while True:
        file_name = input("Enter the sales data filename (e.g., sales_data.csv or sales_data.xlsx): ").strip()
        if os.path.exists(file_name):
            break
        else:
            print(f"Error: File '{file_name}' not found. Please check the filename and path.")

    # Determine file type and read data using pandas
    try:
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_name)
            print(f"Successfully loaded data from '{file_name}' (CSV).")
        elif file_name.endswith('.xlsx'):
            # Bonus: Support Excel (.xlsx)
            df = pd.read_excel(file_name)
            print(f"Successfully loaded data from '{file_name}' (Excel).")
        else:
            print("Error: Unsupported file type. Please provide a .csv or .xlsx file.")
            return

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please ensure it's in the same directory.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_name}' is empty.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # --- Data Processing ---

    # 1. Calculate Revenue for each product entry
    # Ensure 'Units Sold' and 'Unit Price' are numeric
    try:
        df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')
        df['Unit Price'] = pd.to_numeric(df['Unit Price'], errors='coerce')
        # Drop rows where conversion failed (NaN values)
        df.dropna(subset=['Units Sold', 'Unit Price'], inplace=True)
        df['Revenue'] = df['Units Sold'] * df['Unit Price']
    except KeyError:
        print("Error: Missing 'Units Sold' or 'Unit Price' columns in the data.")
        return
    except Exception as e:
        print(f"An error occurred during revenue calculation: {e}")
        return

    # 2. Calculate Total Revenue
    total_revenue = df['Revenue'].sum()

    # 3. Calculate Revenue per Product (grouped)
    product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

    # 4. Identify Top Product
    if not product_revenue.empty:
        top_product = product_revenue.index[0]
        top_product_revenue = product_revenue.iloc[0]
    else:
        top_product = "N/A"
        top_product_revenue = 0.0

    # --- Generate Report Content ---
    report_content = " Sales Summary\n\n"

    # Add individual product revenues to the report
    for product, revenue in product_revenue.items():
        report_content += f"Product: {product} – Revenue: {revenue:.2f}\n"

    report_content += f"\n🔸 Total Revenue: {total_revenue:.2f}\n"
    report_content += f"🔸 Top Product: {top_product}\n"

    # --- Save results in report.txt ---
    report_file_name = "report.txt"
    try:
        with open(report_file_name, 'w') as f:
            f.write(report_content)
        print(f"\nReport successfully saved to '{report_file_name}'.")
    except Exception as e:
        print(f"Error saving report to file: {e}")

    # --- Bonus: Create bar chart with matplotlib ---
    if not product_revenue.empty:
        plt.figure(figsize=(10, 6)) # Set figure size for better readability
        product_revenue.plot(kind='bar', color='skyblue')
        plt.title('Total Revenue by Product')
        plt.xlabel('Product')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45, ha='right') # Rotate labels for better fit
        plt.tight_layout() # Adjust layout to prevent labels from being cut off
        plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a subtle grid
        plt.show() # Display the chart
        print("Bar chart displayed.")
    else:
        print("No product data to display a chart.")

# --- Main execution block ---
if __name__ == "__main__":
    generate_sales_report()
    input("\nPress Enter to exit the program.") # Keeps console open in some environments
