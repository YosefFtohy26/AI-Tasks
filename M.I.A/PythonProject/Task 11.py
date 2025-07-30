import time
import os

def display_gear(gear_number):
    grid = []
    for _ in range(5):
        row = []
        for _ in range(4):
            row.append(' ')
        grid.append(row)

    segments_config = {
        0: ['a', 'b', 'c', 'd', 'e', 'f'],
        1: ['b', 'c'],
        2: ['a', 'b', 'g', 'e', 'd'],
        3: ['a', 'b', 'g', 'c', 'd'],
        4: ['f', 'g', 'b', 'c'],
        5: ['a', 'f', 'g', 'c', 'd'],
        6: ['a', 'f', 'g', 'c', 'd', 'e'],
        7: ['a', 'b', 'c'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    }

    segments_to_light = segments_config.get(gear_number, [])

    if 'a' in segments_to_light:
        for i in range(4):
            grid[0][i] = '#'
    if 'b' in segments_to_light:
        for i in range(1, 3):
            grid[i][3] = '#'
    if 'c' in segments_to_light:
        for i in range(3, 5):
            grid[i][3] = '#'
    if 'd' in segments_to_light:
        for i in range(4):
            grid[4][i] = '#'
    if 'e' in segments_to_light:
        for i in range(3, 5):
            grid[i][0] = '#'
    if 'f' in segments_to_light:
        for i in range(1, 3):
            grid[i][0] = '#'
    if 'g' in segments_to_light:
        for i in range(4):
            grid[2][i] = '#'

    for row in grid:
        print("".join(row))

def clear_screen():
    _ = os.system('cls')


def animate_range(start_gear, end_gear, delay=0.5):

    step = 1 if start_gear <= end_gear else -1

    display_range = range(start_gear, end_gear + step, step)

    for gear in display_range:
        clear_screen()
        print(f"Displaying Gear: {gear}")
        display_gear(gear)
        time.sleep(delay)
    clear_screen()

if __name__ == "__main__":
    while True:
        try:
            range_input = input("Enter gear range (e.g., 0,4) or 'q' to quit: ").lower()

            if range_input == 'q':
                print("Exiting gear display.")
                break

            parts = range_input.split(' ')
            if len(parts) != 2:
                print("Invalid format. Please enter two numbers separated by a comma (e.g., 0,4).")
                continue

            start_gear = int(parts[0].strip())
            end_gear = int(parts[1].strip())

            if 0 <= start_gear <= 8 and 0 <= end_gear <= 8:
                animate_range(start_gear, end_gear)
                print("Range animation complete!")
            else:
                print("Invalid gear numbers. Please enter numbers between 0 and 8.")
        except ValueError:
            print("Invalid input. Please enter integers for the range or 'q'.")
        except IndexError:
            print("Invalid input format. Make sure to enter two numbers separated by a comma.")