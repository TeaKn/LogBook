import runpy

from dataAccess.db import initialize_db


def main() -> None:
    # Run once at startup
    # TODO: Flags for wipeout and data_import should be set to True only when needed, not every time the app starts.
    # therefore have to move them into some sort of variables that live outside of main()
    initialize_db(wipeout=False, data_import=False)
    # change the order of which the data gets imported because of the foreign key constraints.
    # AssessmentType must be imported before Assessment.

    # Start the Bottle app defined in web-interface.py
    runpy.run_path("web-interface.py", run_name="__main__")


if __name__ == '__main__':
    main()
