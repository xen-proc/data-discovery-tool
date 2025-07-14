#!/usr/bin/env python3
"""
Generate test PDF and text files with sensitive data for testing the data discovery tool.
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_with_sensitive_data(output_path):
    """Create a PDF file with various types of sensitive data."""
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Set up the document
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "CONFIDENTIAL - Sensitive Information Test Document")
    
    # Add some regular content
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 120, "This document contains various types of sensitive information")
    c.drawString(72, height - 140, "for testing the data discovery tool.")
    
    # Add sensitive data
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, height - 200, "Customer Records:")
    
    c.setFont("Helvetica", 12)
    y_position = height - 230
    
    # SSN data
    c.drawString(72, y_position, "Name: David Wilson")
    c.drawString(72, y_position - 20, "SSN: 123-45-6789")
    c.drawString(72, y_position - 40, "DOB: 06/12/1975")
    
    # Credit card data
    y_position -= 80
    c.drawString(72, y_position, "Name: Jennifer Adams")
    c.drawString(72, y_position - 20, "Credit Card: 4111 1111 1111 1111")
    c.drawString(72, y_position - 40, "Expiration: 09/26")
    
    # Driver's license data
    y_position -= 80
    c.drawString(72, y_position, "Name: Christopher Lee")
    c.drawString(72, y_position - 20, "Driver's License: D45-678901")
    c.drawString(72, y_position - 40, "State: California")
    
    # Add a mix of data
    y_position -= 100
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y_position, "Combined Sensitive Information:")
    
    c.setFont("Helvetica", 12)
    y_position -= 30
    c.drawString(72, y_position, "Employee: Maria Garcia")
    c.drawString(72, y_position - 20, "ID: 98765")
    c.drawString(72, y_position - 40, "SSN: 987-65-4321")
    c.drawString(72, y_position - 60, "Company Card: 5555-6666-7777-8888")
    c.drawString(72, y_position - 80, "Driver's License: G78-901234")
    
    # Add footer
    c.setFont("Helvetica", 10)  # Using standard Helvetica font
    c.drawString(72, 72, "This document is for testing purposes only.")
    
    # Save the PDF
    c.save()
    print(f"Created test PDF at {output_path}")

def create_text_files_with_sensitive_data(test_data_dir):
    """Create text files with sensitive data."""
    # Create employee records with SSNs
    with open(os.path.join(test_data_dir, "employee_records.txt"), "w") as f:
        f.write("""Employee Records
------------------
Name: John Smith
Position: Software Developer
DOB: 04/12/1985
SSN: 123-45-6789
Annual Salary: $95,000

Name: Sarah Johnson
Position: Project Manager
DOB: 08/23/1979
SSN: 987-65-4321
Annual Salary: $110,000

Name: Michael Lee
Position: System Administrator
DOB: 11/05/1990
SSN: 456-78-9012
Annual Salary: $85,000

Name: Jessica Williams
Position: Data Analyst
DOB: 02/17/1988
SSN: 789-01-2345
Annual Salary: $92,000""")
    
    # Create payment info with credit card numbers
    with open(os.path.join(test_data_dir, "payment_info.txt"), "w") as f:
        f.write("""Customer Payment Information
---------------------------
Customer: Alex Rodriguez
Email: alex.r@example.com
Credit Card: 4111 1111 1111 1111
Expiration: 05/25
Billing Address: 123 Main St, Anytown, CA 94102

Customer: Jamie Wilson
Email: jwilson@example.com
Credit Card: 5500-0000-0000-0004
Expiration: 12/24
Billing Address: 456 Oak Ave, Somecity, CA 94103

Customer: Taylor Greene
Email: tgreene@example.com
Credit Card: 340000000000009
Expiration: 09/26
Billing Address: 789 Pine Blvd, Othercity, CA 94104

Customer: Morgan Smith
Email: msmith@example.com
Credit Card: 6011000990139424
Expiration: 03/27
Billing Address: 101 Redwood Dr, Newcity, CA 94105""")
    
    # Create driver's license records
    with open(os.path.join(test_data_dir, "driver_records.txt"), "w") as f:
        f.write("""Driver License Records
---------------------
Name: Robert Thompson
License #: B1234567
Issue Date: 01/15/2022
Expiration Date: 01/15/2027
Address: 234 Elm Street, Lakeside, CA 92040

Name: Patricia Garcia
License #: G9876543
Issue Date: 07/22/2020
Expiration Date: 07/22/2025
Address: 567 Maple Avenue, Hilltown, CA 93210

Name: William Turner
License #: T54-32109
Issue Date: 03/05/2021
Expiration Date: 03/05/2026
Address: 890 Oak Boulevard, Riverside, CA 92501

Name: Elizabeth Brown
License #: D12-98765
Issue Date: 11/17/2023
Expiration Date: 11/17/2028
Address: 321 Pine Lane, Oceanview, CA 92054""")
    
    # Create mixed data file
    with open(os.path.join(test_data_dir, "mixed_data.txt"), "w") as f:
        f.write("""Customer and Employee Records - CONFIDENTIAL
----------------------------------------
Client: Jordan Miller
Account #: AC-45678
SSN: 567-89-0123
Credit Card: 4444 3333 2222 1111
Driver's License: T23-456789
Contact: j.miller@example.com

Employee: Casey Parker
Employee ID: E-98765
SSN: 321-65-9870
Company Card: 5555-6666-7777-8888
Driver's License: P45-123456
Contact: casey.p@company.com

Vendor: Sam Rodriguez
Vendor ID: V-12345
Tax ID: 123-45-6789
Payment Method: Bank Transfer
Account: 9876543210
Routing: 021000021
Contact: srodriguez@vendor.example.com""")
    
    print(f"Created test text files in {test_data_dir}")

def generate_all_test_data():
    """Generate all test data files."""
    print("=" * 50)
    print("GENERATING TEST DATA")
    print("=" * 50)
    
    # Create the test_data directory if it doesn't exist
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_data_dir = os.path.join(project_root, "test_data")
    os.makedirs(test_data_dir, exist_ok=True)
    
    # Create text files
    create_text_files_with_sensitive_data(test_data_dir)
    
    # Create PDF
    pdf_path = os.path.join(test_data_dir, "sensitive_data.pdf")
    create_pdf_with_sensitive_data(pdf_path)
    
    print("\n" + "=" * 50)
    print("Test data generation completed")
    print("=" * 50)

if __name__ == "__main__":
    generate_all_test_data()
