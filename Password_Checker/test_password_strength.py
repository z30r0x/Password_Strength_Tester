"""
test_password_strength.py

A command-line tool for evaluating password strength using the zxcvbn library.
Supports both single password entry (interactive) and batch analysis from a file.

Usage:
    python test_password_strength.py              # interactive single password
    python test_password_strength.py <file>       # batch mode from a file
"""

from zxcvbn import zxcvbn
import getpass
import sys


def test_single_password():
    """
    Prompt the user to enter a single password securely (input is hidden),
    then analyse and display its strength score, estimated crack time,
    and improvement suggestions.
    """
    # getpass hides the typed characters so the password isn't visible on screen
    password = getpass.getpass("[?] Enter your password: ")

    # Run the zxcvbn strength analysis
    result = zxcvbn(password)
    print(f"Value:      {result['password']}")
    print(f"Score:      {result['score']}/4")
    # Use the slow offline hashing scenario — a realistic worst-case attacker estimate
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"Feedback:   {result['feedback']['suggestions']}")


def test_multiple_passwords(password_file):
    """
    Read passwords line-by-line from a plain-text file and print a strength
    report for each one.

    Args:
        password_file (str): Path to a file containing one password per line.
    """
    try:
        with open(password_file, 'r') as passwords:
            for password in passwords:
                # Strip the trailing newline so it doesn't affect the analysis
                result = zxcvbn(password.strip('\n'))

                print('\n[+] ######################')  # visual separator between entries
                print(f"Value:      {result['password']}")
                print(f"Score:      {result['score']}/4")
                print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
                print(f"Feedback:   {result['feedback']['suggestions']}")

    except FileNotFoundError:
        print(f"[!] File not found: '{password_file}'. Please check the path and try again.")
    except PermissionError:
        print(f"[!] Permission denied reading '{password_file}'.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")


# ── Entry point ───────────────────────────────────────────────────────────────

if len(sys.argv) == 2:
    # A file path was provided — run in batch mode
    test_multiple_passwords(sys.argv[1])
elif len(sys.argv) == 1:
    # No arguments — run in interactive single-password mode
    test_single_password()
else:
    print(
        "Usage:\n"
        "  python test_password_strength.py              "
        "# analyse a single password interactively\n"
        "  python test_password_strength.py <file>       "
        "# analyse every password in a file"
    )