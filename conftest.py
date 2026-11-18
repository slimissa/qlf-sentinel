import sys
import os

# Adds the current directory to sys.path so tests can find the 'src' module
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
