"""
Classification functionality for sensitive data.
"""

from enum import Enum

class DataClassification(Enum):
    PUBLIC = "Public"
    INTERNAL = "Internal"
    CONFIDENTIAL = "Confidential"
    RESTRICTED = "Restricted"

def classify_data(pattern_name):
    """
    Classifies the data based on the pattern name.
    
    Args:
        pattern_name: Name of the pattern matched.
        
    Returns:
        str: Classification level as string.
    """
    if pattern_name in ["Social Security Number", "Credit Card Number", "Driver's License"]:
        return DataClassification.RESTRICTED.value
    else:
        return DataClassification.PUBLIC.value
