import sys
import os

# Ensure the root directory is in the PYTHONPATH so imports work perfectly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.db_setup import initialize_database
from gui.auth_window import AuthWindow

def main():
    # 1. Initialize DB (creates DB and tables if missing)
    initialize_database()

    # 2. Launch the GUI
    app = AuthWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
