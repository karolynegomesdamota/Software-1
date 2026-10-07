# Import
import time

# This function prints a table with all the items the character has.

def print_panel (items):
    print(f"{'\nItems':<15}{'Amount':<10}")
    print("-" * 20)
    print(f"{'Seeds':<15}{items['seeds']:<10}")
    print(f"{'Money':<15}{items['money']:<10}")
    print(f"{'Trees':<15}{items['trees']:<10}")
    print(f"{'Water':<15}{items['water']:<10}")
    print(f"{'Jackets':<15}{items['jacket']:<10}")
    print(f"{'Boats':<15}{items['boat']:<10}")
    time.sleep(1)