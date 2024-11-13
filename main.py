from presentation import Presentation

if __name__ == "__main__":
    """
    Entry point for the application.

    This module initializes the Presentation layer and starts the main menu loop, 
    allowing users to interact with the application for managing records.
    """
    app = Presentation()
    while True:
        app.display_menu()
