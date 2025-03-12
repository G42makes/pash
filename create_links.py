#!/usr/bin/env python3
"""
Utility script to create symlinks (or equivalent) for pash.py in different modes.
This is particularly helpful on Windows which doesn't easily support symbolic links.
"""

import os
import sys
import platform
import shutil


def create_link(target, link_name):
    """
    Create a symlink or equivalent based on the platform.
    
    Args:
        target: The target file to link to
        link_name: The name of the link to create
    """
    print(f"Creating link: {link_name} -> {target}")
    
    if platform.system() == "Windows":
        # On Windows, create a batch file that calls the Python script
        with open(f"{link_name}.bat", "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python {target} --mode {link_name}\n")
        print(f"Created {link_name}.bat")
    else:
        # On Unix-like systems, create a symbolic link
        try:
            if os.path.exists(link_name):
                os.remove(link_name)
            os.symlink(target, link_name)
            # Make the link executable
            os.chmod(link_name, 0o755)
            print(f"Created symlink: {link_name}")
        except Exception as e:
            print(f"Error creating symlink: {e}")
            print("You might need administrative privileges or use a different approach.")


def main():
    """Create the necessary links for different shell modes."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(script_dir, "src", "pash.py")
    
    # Ensure the target exists
    if not os.path.exists(target):
        print(f"Error: Target file {target} not found.")
        return 1
    
    # Create links for each mode
    create_link(target, "pash")
    create_link(target, "bash")
    create_link(target, "sh")
    
    print("\nLinks created successfully. You can now run the shell using:")
    print("- 'pash' for Pash mode")
    print("- 'bash' for Bash-compatible mode")
    print("- 'sh' for basic shell mode")


if __name__ == "__main__":
    sys.exit(main()) 