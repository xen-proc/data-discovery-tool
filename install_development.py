#!/usr/bin/env python3
"""
Helper script to install the package in development mode
and make it ready for testing after the reorganization.
"""

import os
import sys
import subprocess
import shutil

def main():
    """Install the package in development mode and set up the test data."""
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 50)
    print("Setting up Data Discovery Tool development environment")
    print("=" * 50)
    
    # Create virtual environment if it doesn't exist
    venv_dir = os.path.join(project_root, "venv")
    if not os.path.exists(venv_dir):
        print("\nCreating virtual environment...")
        try:
            subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
            print("Virtual environment created successfully.")
        except subprocess.CalledProcessError:
            print("Error: Failed to create virtual environment.")
            return 1
    
    # Determine the activate script path based on platform
    if sys.platform == "win32":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
        activate_cmd = f"{activate_script}"
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        activate_cmd = f"source {activate_script}"
    
    # Install the package in development mode
    print("\nInstalling package in development mode...")
    print(f"Run: {activate_cmd} && pip install -e .")
    print("\nThis will make the package available for import from anywhere.")
    
    # Generate test data
    print("\nTo generate test data, run:")
    print(f"{activate_cmd} && python -m tests.generate_test_data")
    
    # Run tests
    print("\nTo run tests:")
    print(f"{activate_cmd} && python -m tests.test_discovery")
    print(f"{activate_cmd} && python -m tests.test_pdf_scan")
    print(f"{activate_cmd} && python -m tests.test_json_output")
    
    # Run the tool
    print("\nTo run the data discovery tool:")
    print(f"{activate_cmd} && python -m scripts.run_discovery /path/to/scan -o results.json")
    
    print("\n" + "=" * 50)
    print("Setup instructions completed. See README.md for more details.")
    print("=" * 50)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
