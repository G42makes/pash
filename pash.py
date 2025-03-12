#!/usr/bin/env python3
"""
Entry point for Pash shell.
This script simply imports and runs the main pash module from the src directory.
"""

import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

# Import and run main
from pash import main

if __name__ == "__main__":
    main() 