#!/usr/bin/env python3
"""
Setup script for the data discovery tool.
"""

from setuptools import setup, find_packages

setup(
    name="data_discovery",
    version="0.1.0",
    description="A tool for discovering sensitive data in files",
    author="Shawn Paul & Claude",
    packages=find_packages(),
    install_requires=[
        "PyPDF2>=3.0.0",
        "reportlab>=4.0.0",
    ],
    entry_points={
        'console_scripts': [
            'data-discovery=scripts.run_discovery:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
