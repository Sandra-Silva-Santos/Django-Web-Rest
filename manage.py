#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the environment variable for the Django settings module.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
    try:
        # Import the execute_from_command_line() function from the
        # django.core.management module.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If the import fails, raise an ImportError exception and
        # include a custom message.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Call execute_from_command_line() to execute the command-line
    # utility.
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
