import sys
from pywinauto import Application

def click_by_internal_label(target_label):
    try:
        app = Application(backend="uia").connect(title_re=".*Focus Bear.*", visible_only=True)
        main_window = app.window(title_re=".*Focus Bear.*", visible_only=True, found_index=0)
        main_window.set_focus()

        # We look for any descendant that has the title you see in the identifiers
        # This will search through the 'NavLeaf' children automatically
        target = main_window.child_window(title=target_label, control_type="Text")
        
        if not target.exists():
            # Sometimes labels are 'Static' types instead of 'Text'
            target = main_window.child_window(title=target_label, control_type="Static")

        print(f"Targeting: {target_label}")
        
        # We click the parent NavLeaf to ensure the whole button registers the hit
        target.parent().click_input()
        print(f"SUCCESS: {target_label} clicked via its child label.")

    except Exception as e:
        print(f"ERROR: Could not find label '{target_label}'. Details: {e}")

if __name__ == "__main__":
    # Test it the habits page
    click_by_internal_label("Habits")