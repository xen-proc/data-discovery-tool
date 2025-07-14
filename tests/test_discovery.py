#!/usr/bin/env python3
"""
Test script for data discovery tool.
Scans the test_data directory for sensitive information.
"""

import os
import sys
import json
from data_discovery.scanner import find_sensitive_data, scan_directory, write_results_to_json

def run_test():
    """
    Run tests on the data discovery tool using the test_data directory.
    """
    print("=" * 50)
    print("DATA DISCOVERY TOOL TEST")
    print("=" * 50)
    
    # Get the absolute path to the test_data directory
    test_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
    
    if not os.path.isdir(test_dir):
        print(f"Error: Test directory '{test_dir}' not found.")
        sys.exit(1)
        
    print(f"Scanning directory: {test_dir}")
    print("-" * 50)
    
    # Test individual files
    print("\nTesting individual file scans:")
    test_files = [
        "employee_records.txt",
        "payment_info.txt",
        "driver_records.txt",
        "mixed_data.txt"
    ]
    
    total_findings = 0
    for file in test_files:
        file_path = os.path.join(test_dir, file)
        if os.path.exists(file_path):
            print(f"\nScanning {file}:")
            results = find_sensitive_data(file_path)
            total_findings += len(results)
        else:
            print(f"File not found: {file}")
    
    # Test directory scan
    print("\n" + "=" * 50)
    print("Testing directory scan:")
    print("-" * 50)
    all_results = scan_directory(test_dir)
    
    print(f"\nTotal findings in directory scan: {len(all_results)}")
    
    # Optional JSON output test
    output_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_results.json")
    write_results_to_json(all_results, output_file)
    
    print("\n" + "=" * 50)
    print("Test completed")
    print("=" * 50)

if __name__ == "__main__":
    run_test()
