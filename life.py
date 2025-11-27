#!/usr/bin/env python3
"""
Life Board - A terminal-based visualization of your life in weeks.
Displays 80 years of life (4160 weeks total), shading in the weeks you've lived.
"""

from datetime import datetime, timedelta

# Birth date
BIRTH_DATE = datetime(2002, 5, 22)
TOTAL_WEEKS = 80 * 52  # 80 years * 52 weeks
WEEKS_PER_ROW = 104    # 104 weeks per row (2 years)

# Characters for display
FILLED_BOX = "█"
EMPTY_BOX = "░"


def calculate_weeks_lived():
    """Calculate how many weeks have been lived since birth."""
    today = datetime.now()
    days_lived = (today - BIRTH_DATE).days
    weeks_lived = days_lived // 7
    return weeks_lived


def display_life_board():
    """Display the life board in the terminal."""
    weeks_lived = calculate_weeks_lived()
    weeks_remaining = TOTAL_WEEKS - weeks_lived

    # Calculate border width (age label + spaces + weeks)
    border_width = 11 + WEEKS_PER_ROW
    border = "═" * border_width

    # Display header
    title = "WEEKS OF MY LIFE"
    title_padding = (border_width - len(title)) // 2
    print("\n" + border)
    print(" " * title_padding + title)
    print(border)

    # Display the grid
    for row in range(40):
        row_output = ""
        for col in range(104):
            week_number = row * 104 + col
            if week_number < weeks_lived:
                row_output += FILLED_BOX
            else:
                row_output += EMPTY_BOX

        # Add age label on the left
        age_start = row * 2
        age_end = age_start + 1
        print(f"Age {age_start:2d}-{age_end:2d}  {row_output}")

    # Display footer with stats
    print(border)
    print(f"Weeks lived:      {weeks_lived:5d}")
    print(f"Weeks remaining:  {weeks_remaining:5d}")
    print(f"Total weeks:      {TOTAL_WEEKS:5d}")
    print(border)

    # Calculate and display percentage
    percentage_lived = (weeks_lived / TOTAL_WEEKS) * 100
    print(f"Your life is {percentage_lived:.1f}% over.\n")


if __name__ == "__main__":
    display_life_board()
