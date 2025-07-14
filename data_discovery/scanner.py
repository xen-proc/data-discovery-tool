"""
Core scanning functionality for data discovery tool.
"""

import os
import re
import json
from datetime import datetime

from data_discovery.config import SENSITIVE_DATA_PATTERNS
from data_discovery.classification import classify_data
from data_discovery.utils.pdf_utils import extract_text_from_pdf

def find_sensitive_data(file_path):
    """
    Scans a file for sensitive data patterns.
    Supports both text and PDF files.
    
    Args:
        file_path: Path to the file to scan.
        
    Returns:
        A list of dictionaries containing detected sensitive data information.
    """
    results = []
    
    try:
        # Check if the file is a PDF
        if file_path.lower().endswith('.pdf'):
            content = extract_text_from_pdf(file_path)
        else:
            # Process as a regular text file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # Skip binary files that aren't PDFs
                return results
                
        # Search for patterns in the content
        for pattern_name, regex in SENSITIVE_DATA_PATTERNS.items():
            matches = re.finditer(regex, content)
            for match in matches:
                classification = classify_data(pattern_name)
                # Get some context around the match (30 chars before and after)
                start = max(0, match.start() - 30)
                end = min(len(content), match.end() + 30)
                context = content[start:end].replace('\n', ' ')
                
                result = {
                    'file_path': file_path,
                    'pattern_name': pattern_name,
                    'classification': classification,
                    'match': match.group(),
                    'context': context,
                    'line_number': content[:match.start()].count('\n') + 1
                }
                results.append(result)
                print(f"Found {pattern_name} in {file_path} - Classification: {classification}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        
    return results

def scan_directory(directory):
    """
    Recursively scans a directory for files and checks them for sensitive data.
    
    Args:
        directory: Directory path to scan.
        
    Returns:
        A list of dictionaries containing detected sensitive data information.
    """
    all_results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            results = find_sensitive_data(file_path)
            if results:
                all_results.extend(results)
    return all_results

def write_results_to_json(results, json_file):
    """
    Writes scan results to a JSON file.
    
    Args:
        results: List of result dictionaries
        json_file: Path to output JSON file
    """
    output_data = {
        'scan_time': datetime.now().isoformat(),
        'total_findings': len(results),
        'findings': results
    }
    
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4)
        print(f"\nResults written to {json_file}")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")
