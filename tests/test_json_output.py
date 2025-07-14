#!/usr/bin/env python3
"""
Test script for JSON output functionality in the data discovery tool.
"""

import os
import json
from data_discovery.scanner import scan_directory, write_results_to_json

def test_json_output():
    """
    Test the JSON output functionality of the data discovery tool.
    """
    print("=" * 50)
    print("JSON OUTPUT TEST")
    print("=" * 50)
    
    # Get the path to the test data directory
    test_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
    output_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scan_results.json")
    
    print(f"Scanning directory: {test_dir}")
    print("-" * 50)
    
    # Scan the test directory
    results = scan_directory(test_dir)
    
    # Write the results to JSON
    write_results_to_json(results, output_file)
    
    # Read and display the JSON file contents
    print("\nJSON output sample:")
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
            print(f"Scan time: {data['scan_time']}")
            print(f"Total findings: {data['total_findings']}")
            
            # Print the first 3 findings as a sample
            print("\nSample findings:")
            for i, finding in enumerate(data['findings'][:3], 1):
                print(f"\nFinding {i}:")
                print(f"  File: {os.path.basename(finding['file_path'])}")
                print(f"  Pattern: {finding['pattern_name']}")
                print(f"  Classification: {finding['classification']}")
                print(f"  Match: {finding['match']}")
                print(f"  Line number: {finding['line_number']}")
                print(f"  Context: {finding['context'][:50]}..." if len(finding['context']) > 50 else f"  Context: {finding['context']}")
            
            if data['total_findings'] > 3:
                print(f"\n... and {data['total_findings'] - 3} more findings.")
    
    except Exception as e:
        print(f"Error reading JSON output: {e}")
    
    print("\n" + "=" * 50)
    print("JSON output test completed")
    print("=" * 50)

if __name__ == "__main__":
    test_json_output()
