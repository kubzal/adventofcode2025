import os
import requests

from dotenv import load_dotenv

from icecream import ic


def load_example():
    return """3-5
            10-14
            16-20
            12-18

            1
            5
            8
            11
            17
            32
    """


def load_input(
    url="https://adventofcode.com/2025/day/5/input", filename="day05_input.txt"
) -> list:
    if os.path.exists(filename):
        print(f"Loading input from file: {filename}")
        with open(filename, "r") as f:
            return f.read().strip().splitlines()
    else:
        print(f"Downloading input from website: {url}")
        load_dotenv()
        cookies = {"session": os.getenv("AOC_SESSION")}
        response = requests.get(url, cookies=cookies)
        with open(filename, "w") as f:
            f.write(response.text.strip())
        return response.text.strip().splitlines()


def load_ranges_and_ingredients(example: bool = False) -> tuple:
    if not example:
        data = "\n".join(load_input())
    else:
        data = load_example()

    ranges = list()
    ingredients = list()

    end_of_ranges = False
    for line in data.split("\n"):
        line = line.strip()

        if len(line) == 0:
            end_of_ranges = True
            continue

        if not end_of_ranges:
            upper_str, lower_str = line.split("-")
            upper = int(upper_str)
            lower = int(lower_str)
            ranges.append((upper, lower))

        if end_of_ranges:
            ingredients.append(int(line))

    return ranges, ingredients


def squash_ranges(ranges: list) -> list:
    ranges_squashed = list()

    for upper, lower in sorted(ranges):
        if not ranges_squashed:
            ranges_squashed.append((upper, lower))
            continue

        last_upper, last_lower = ranges_squashed[-1]

        if upper <= last_lower + 1:
            ranges_squashed[-1] = (last_upper, max(last_lower, lower))
        else:
            ranges_squashed.append((upper, lower))

    return ranges_squashed


def count_total_ingredients_considered_to_be_fresh(ranges: list):
    total = 0
    for upper, lower in ranges:
        total += (lower - upper) + 1
    return total
    

def check_ingredients_freshness(ranges: list, ingredients: list) -> int:
    fresh_ingredients = list()
    for ingredient in ingredients:
        for upper, lower in ranges:
            if upper <= ingredient <= lower:
                fresh_ingredients.append(ingredient)
    return len(set(fresh_ingredients))


def main():
    ranges, ingredients = load_ranges_and_ingredients()
    ranges = squash_ranges(ranges)
    fresh_ingredients = check_ingredients_freshness(ranges, ingredients)
    print("Part 1:")
    print(f"Fresh ingredients: {fresh_ingredients}")

    total_ingredients = count_total_ingredients_considered_to_be_fresh(ranges)

    print()
    print("Part 2:")
    print(f"TOTAL IDs considered to be fresh: {total_ingredients}")

if __name__ == "__main__":
    main()
