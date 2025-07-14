"""
Configuration for data discovery tool.
"""

# Regular expression patterns for sensitive data detection
SENSITIVE_DATA_PATTERNS = {
    "Social Security Number": r"\b\d{3}-\d{2}-\d{4}\b",
    "Credit Card Number": r"\b(?:\d{4}[ -]?){3}\d{4}\b",
    "Driver's License": r"\b[A-Z]\d{1,2}[- ]?\d{4,8}\b",
}
