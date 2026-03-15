# Data Discovery Tool

A Python tool for detecting sensitive personally identifiable information (PII) in files. The tool scans both text files and PDFs to identify patterns like Social Security Numbers, credit card numbers, and driver's license numbers.

Primarily built for education and learning purposes. 

## Features

- **Sensitive data detection** using regular expression patterns
- **PDF scanning** with text extraction capabilities
- **Detailed findings** with context around matched patterns
- **Classification system** (Public, Internal, Confidential, Restricted)
- **JSON output** for integration with other systems
- **Command-line interface** for easy use

## Todo
- Add support for scanning databases
- Add support for scanning cloud storage (e.g. AWS S3)

## Project Structure

```
data_discovery_tool/
│
├── data_discovery/            # Main package directory
│   ├── __init__.py            # Package initialization
│   ├── scanner.py             # Core scanning functionality
│   ├── classification.py      # Data classification functionality
│   ├── config.py              # Pattern configurations
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       └── pdf_utils.py       # PDF handling functionality
│
├── scripts/                   # Command-line scripts
│   └── run_discovery.py       # Entry point script
│
├── tests/                     # Test directory
│   ├── __init__.py
│   ├── test_discovery.py      # Main discovery tests
│   ├── test_pdf_scan.py       # PDF scanning tests
│   ├── test_json_output.py    # JSON output tests
│   └── generate_test_data.py  # Test data generation
│
└── test_data/                 # Test data directory
    ├── employee_records.txt   # Contains fake SSNs
    ├── payment_info.txt       # Contains fake credit card numbers
    ├── driver_records.txt     # Contains fake driver's license numbers
    ├── mixed_data.txt         # Contains multiple types of sensitive data
    └── sensitive_data.pdf     # PDF with sensitive data
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd data_discovery_tool
   ```

2. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package:
   ```
   pip install -e .
   ```

## Usage

### Command Line Interface

Scan a directory for sensitive data:

```
data-discovery /path/to/directory
```

Output results to a JSON file:

```
data-discovery /path/to/directory -o results.json
```

### Using as a Python Package

```python
from data_discovery.scanner import scan_directory, write_results_to_json

# Scan a directory
results = scan_directory("/path/to/directory")

# Output results to JSON
write_results_to_json(results, "results.json")
```

## Development

### Generate Test Data

```
python -m tests.generate_test_data
```

### Run Tests

```
python -m tests.test_discovery
python -m tests.test_pdf_scan
python -m tests.test_json_output
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
