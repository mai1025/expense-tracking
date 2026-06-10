import sys
import os

# To Get the absolute path of the 'expense_tracking' (root) directory
#   > __file__ gets current working file path '../expense_tracking/tests/conftest.py'
#   > os.path.dirname(__filename__) gets directory for the file '../expense_tracking/tests'
#   > Since conftest.py is in /tests, we need to go up one level to get root
#       > adding '..' to the directory goes up one level so gets /expense_tracking
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add it to sys.path if it's not already there
if root_path not in sys.path:
    sys.path.insert(0, root_path)