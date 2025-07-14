#!/usr/bin/env python3
"""
Test script specifically for testing PDF scanning functionality in the data discovery tool.
"""

import os
import sys
from data_discovery.scanner import find_sensitive_data
from data_discovery.utils.pdf_utils import extract_text_from_pdf

def test_pdf_scanning():
    """
    Test the PDF scanning functionality of the data discovery tool.
    """
    print("=" * 50)
    print("PDF SCANNING TEST")
    print("=" * 50)
    
    # Get the path to the test PDF file
    test_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
    pdf_file = os.path.join(test_dir, "sensitive_data.pdf")
    
    if not os.path.exists(pdf_file):
        print(f"Error: Test PDF file '{pdf_file}' not found.")
        sys.exit(1)
    
    # Test PDF text extraction
    print("\nTesting PDF text extraction...")
    extracted_text = extract_text_from_pdf(pdf_file)
    
    # Print a sample of the extracted text
    print("\nSample of extracted text:")
    print("-" * 50)
    print(extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text)
    print("-" * 50)
    
    # Test sensitive data detection in PDF
    print("\nTesting sensitive data detection in PDF...")
    results = find_sensitive_data(pdf_file)
    print(f"Found {len(results)} instances of sensitive data in the PDF.")
    
    print("\n" + "=" * 50)
    print("PDF scanning test completed")
    print("=" * 50)

if __name__ == "__main__":
    test_pdf_scanning()
