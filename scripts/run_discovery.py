#!/usr/bin/env python3
"""
Command-line entry point for data discovery tool.
"""

import argparse
import os
import sys
from data_discovery.scanner import scan_directory, write_results_to_json

def main():
    """
    Main function to parse arguments and start the scanning process.
    """
    parser = argparse.ArgumentParser(description="Sensitive Data Discovery Tool")
    parser.add_argument("directory", help="The directory to scan for sensitive data.")
    parser.add_argument("-o", "--output", help="Path to JSON output file")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory.")
        return 1

    print(f"Scanning directory: {args.directory}")
    print("-" * 50)
    
    # Scan the directory and get results
    results = scan_directory(args.directory)
    
    # Print summary
    print(f"\nScan complete. Found {len(results)} instances of sensitive data.")
    
    # Write to JSON if output file is specified
    if args.output:
        write_results_to_json(results, args.output)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
