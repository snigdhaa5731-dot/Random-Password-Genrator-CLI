#!/usr/bin/env python3
"""
Random Password Generator (CLI - Beginner Tier)
Meets all criteria defined in req.txt:
- Configurable password length (minimum 8 characters enforced)
- Character type selection: uppercase, lowercase, numbers, symbols (at least 2 types required)
- Input validation with user-friendly error messages
- Option to generate multiple passwords without restarting
"""

import random
import string
import sys


def get_character_sets() -> dict[str, str]:
    """Return the available character sets mapped by key."""
    return {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "numbers": string.digits,
        "symbols": string.punctuation,
    }


def generate_password(
    length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generate a random password matching the criteria.

    Parameters:
        length (int): Total length of the password (minimum 8 characters).
        use_upper (bool): Include uppercase letters (A-Z).
        use_lower (bool): Include lowercase letters (a-z).
        use_digits (bool): Include numeric digits (0-9).
        use_symbols (bool): Include punctuation symbols (!@#$...).

    Returns:
        str: Generated password string.

    Raises:
        ValueError: If length < 8 or fewer than 2 character sets are selected.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    char_sets = get_character_sets()
    selected_pools = []

    if use_upper:
        selected_pools.append(char_sets["uppercase"])
    if use_lower:
        selected_pools.append(char_sets["lowercase"])
    if use_digits:
        selected_pools.append(char_sets["numbers"])
    if use_symbols:
        selected_pools.append(char_sets["symbols"])

    if len(selected_pools) < 2:
        raise ValueError("At least 2 character types must be selected.")

    # Guarantee at least one character from each selected category
    password_chars = [random.choice(pool) for pool in selected_pools]

    # Combine all selected characters into a single pool for the remaining characters
    combined_pool = "".join(selected_pools)
    remaining_length = length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(random.choice(combined_pool))

    # Shuffle the characters so guaranteed characters aren't always at the start
    random.shuffle(password_chars)

    return "".join(password_chars)


def prompt_yes_no(question: str, default: bool = True) -> bool:
    """Prompt user for a yes/no answer with validation."""
    hint = " [Y/n]: " if default else " [y/N]: "
    while True:
        try:
            raw = input(f"{question}{hint}").strip().lower()
        except EOFError:
            print()
            return default

        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  [!] Please enter 'y' for yes or 'n' for no.")


def prompt_length(min_length: int = 8) -> int:
    """Prompt user for a valid password length (>= min_length)."""
    while True:
        try:
            user_input = input(f"Enter desired password length (minimum {min_length}): ").strip()
            length = int(user_input)
            if length < min_length:
                print(f"  [!] Invalid length: must be at least {min_length} characters. Try again.")
                continue
            return length
        except ValueError:
            print("  [!] Invalid input: please enter a valid positive integer.")
        except EOFError:
            print("\nExiting program.")
            sys.exit(0)


def prompt_character_types() -> tuple[bool, bool, bool, bool]:
    """Prompt user to choose character types until at least 2 are selected."""
    while True:
        print("\nChoose character types to include (at least 2 required):")
        use_upper = prompt_yes_no("  Include uppercase letters (A-Z)?", default=True)
        use_lower = prompt_yes_no("  Include lowercase letters (a-z)?", default=True)
        use_digits = prompt_yes_no("  Include numbers (0-9)?", default=True)
        use_symbols = prompt_yes_no("  Include symbols (!@#$%^&*...)?", default=True)

        selected_count = sum([use_upper, use_lower, use_digits, use_symbols])
        if selected_count >= 2:
            return use_upper, use_lower, use_digits, use_symbols

        print(
            f"\n  [!] Selection error: You selected {selected_count} character type(s)."
            "\n      At least 2 types must be selected. Please choose again."
        )


def run_cli():
    """Main CLI execution loop."""
    print("=" * 50)
    print("       RANDOM PASSWORD GENERATOR (CLI)")
    print("=" * 50)

    while True:
        try:
            length = prompt_length(min_length=8)
            use_upper, use_lower, use_digits, use_symbols = prompt_character_types()

            password = generate_password(
                length=length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_symbols=use_symbols,
            )

            print("\n" + "-" * 50)
            print("Generated Password:")
            print(f"  >>> {password} <<<")
            print(f"Length: {len(password)} characters")
            print("-" * 50)

            if not prompt_yes_no("\nWould you like to generate another password?", default=True):
                print("\nThank you for using the Random Password Generator. Goodbye!\n")
                break
            print("\n" + "=" * 50)

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!\n")
            sys.exit(0)


if __name__ == "__main__":
    run_cli()
