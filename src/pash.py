#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pash - Python implementation of Bash/Sh shell.

Supports three modes:
- sh: Basic POSIX shell
- bash: Bash-compatible shell
- pash: Extended Bash with Python integration
"""

import os
import sys
import argparse
from typing import Optional


class PashShell:  # pylint: disable=too-few-public-methods
    """Main class for the Pash shell implementation."""

    MODE_SH = "sh"
    MODE_BASH = "bash"
    MODE_PASH = "pash"

    def __init__(self, mode: Optional[str] = None):
        """
        Initialize the shell with the specified mode.

        Args:
            mode: One of 'sh', 'bash', or 'pash'. If None, auto-detected.
        """
        self.mode = self._determine_mode(mode)
        print(f"Starting Pash in {self.mode} mode")

    def _determine_mode(self, mode: Optional[str]) -> str:
        """
        Determine the shell mode based on parameters and invocation.

        Args:
            mode: Explicitly requested mode, if any.

        Returns:
            The determined mode (sh, bash, or pash).
        """
        if mode and mode in [self.MODE_SH, self.MODE_BASH, self.MODE_PASH]:
            return mode

        # Determine mode based on invocation name
        invocation = os.path.basename(sys.argv[0])
        if invocation in ("sh", "sh.py"):
            return self.MODE_SH
        if invocation in ("bash", "bash.py"):
            return self.MODE_BASH
        # Default to pash mode
        return self.MODE_PASH

    def run(self):
        """Run the shell's main loop."""
        try:
            while True:
                # Simple command input for now
                prompt = self._get_prompt()
                cmd = input(prompt)
                
                if cmd.lower() in ["exit", "quit"]:
                    break
                
                print(f"Would execute: {cmd}")
        except KeyboardInterrupt:
            print("\nExiting...")
        except EOFError:
            print("\nExiting...")

    def _get_prompt(self) -> str:
        """
        Get the appropriate prompt string based on mode.

        Returns:
            The prompt string to display.
        """
        if self.mode == self.MODE_SH:
            return "$ "
        if self.mode == self.MODE_BASH:
            return "bash$ "
        # pash mode
        return "pash$ "


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Python implementation of Bash/Sh shell')
    parser.add_argument('--mode', choices=['sh', 'bash', 'pash'],
                        help='Shell mode to run in (sh, bash, or pash)')
    return parser.parse_args()


def main():
    """Main entry point for the Pash shell."""
    args = parse_args()
    shell = PashShell(mode=args.mode)
    shell.run()


if __name__ == "__main__":
    main() 