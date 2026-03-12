from pywinauto import Application, Desktop
from contextlib import redirect_stdout

def test_connection():
    print("--- Searching for Focus Bear ---")
    
    try:
        # 1. Try to connect to an already running instance
        # We use a regex for the title because it might change (e.g., "Focus Bear - Morning Routine")
        app = Application(backend="uia").connect(title_re=".*Focus Bear.*", timeout=5)
        main_window = app.window(title_re=".*Focus Bear.*")
        
        print(f"SUCCESS: Connected to Focus Bear (PID: {app.process})")
        
        # 2. Dump the UI tree
        # This is the most important part; it shows you what OpenClaw can 'touch'

        with open("Identifier List", "w", encoding="utf-8") as f:
            with redirect_stdout(f):
                main_window.print_control_identifiers()
        
        
    except Exception as e:
        print(f"FAILED: Could not connect to Focus Bear.")
        print(f"Error Details: {e}")
        print("\nTIP: Make sure Focus Bear is open and visible on your screen.")

if __name__ == "__main__":
    test_connection()