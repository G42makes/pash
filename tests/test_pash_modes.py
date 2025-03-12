#!/usr/bin/env python3
"""
Tests for the Pash shell mode detection functionality.
"""

import os
import sys
import unittest
from unittest.mock import patch
import tempfile
import shutil

# Add the src directory to the Python path to allow importing pash
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from pash import PashShell


class TestPashModes(unittest.TestCase):
    """Test cases for Pash shell mode detection."""

    def setUp(self):
        """Set up test environment."""
        self.original_argv0 = sys.argv[0]
        
    def tearDown(self):
        """Restore original sys.argv[0]."""
        sys.argv[0] = self.original_argv0

    def test_explicit_mode_sh(self):
        """Test explicit 'sh' mode detection."""
        shell = PashShell(mode="sh")
        self.assertEqual(shell.mode, "sh")

    def test_explicit_mode_bash(self):
        """Test explicit 'bash' mode detection."""
        shell = PashShell(mode="bash")
        self.assertEqual(shell.mode, "bash")

    def test_explicit_mode_pash(self):
        """Test explicit 'pash' mode detection."""
        shell = PashShell(mode="pash")
        self.assertEqual(shell.mode, "pash")

    def test_implicit_mode_sh(self):
        """Test implicit 'sh' mode detection from filename."""
        sys.argv[0] = "sh"
        shell = PashShell()
        self.assertEqual(shell.mode, "sh")

    def test_implicit_mode_bash(self):
        """Test implicit 'bash' mode detection from filename."""
        sys.argv[0] = "bash"
        shell = PashShell()
        self.assertEqual(shell.mode, "bash")

    def test_implicit_mode_pash_default(self):
        """Test implicit 'pash' mode detection (default)."""
        sys.argv[0] = "something_else"
        shell = PashShell()
        self.assertEqual(shell.mode, "pash")

    def test_prompt_format_sh(self):
        """Test that the prompt format is correct for sh mode."""
        shell = PashShell(mode="sh")
        self.assertEqual(shell._get_prompt(), "$ ")

    def test_prompt_format_bash(self):
        """Test that the prompt format is correct for bash mode."""
        shell = PashShell(mode="bash")
        self.assertEqual(shell._get_prompt(), "bash$ ")

    def test_prompt_format_pash(self):
        """Test that the prompt format is correct for pash mode."""
        shell = PashShell(mode="pash")
        self.assertEqual(shell._get_prompt(), "pash$ ")


if __name__ == "__main__":
    unittest.main() 