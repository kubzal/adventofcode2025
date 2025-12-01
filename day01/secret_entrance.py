# Description: https://adventofcode.com/2025/day/1

import os
import requests

from dotenv import load_dotenv


def load_input(
    url="https://adventofcode.com/2025/day/1/input", filename="day01_input.txt"
):
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


# Part 1
def dial(position: int = 0, rotation: str = "L1"):
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "L":
        return (position - distance) % 100

    if direction == "R":
        return (position + distance) % 100


# Part 2 (brute force)
def hit_zero_brute_force(position: int = 0, rotation: str = "L1"):
    direction = rotation[0]
    distance = int(rotation[1:])

    zeros = 0
    points = range(1, distance + 1)

    if direction == "L":
        for k in points:
            if (position - k) % 100 == 0:
                zeros += 1

    if direction == "R":
        for k in points:
            if (position + k) % 100 == 0:
                zeros += 1
    return zeros


# Part 2 (more optimal solution)
def hit_zero_more_optimal(position: int = 0, rotation: str = "L1"):
    direction = rotation[0]
    distance = int(rotation[1:])

    for k in range(1, distance + 1):
        if ((direction == "L") & ((position - k) % 100 == 0)) | (
            (direction == "R") & ((position + k) % 100 == 0)
        ):
            return 1 + (distance - k) // 100
    return 0


# Part 2
def hit_zero(position: int = 0, rotation: str = "L1") -> int:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "R":
        k0 = (100 - position) % 100
        if k0 == 0:
            k0 = 100
    else:  # "L"
        k0 = position % 100
        if k0 == 0:
            k0 = 100

    if k0 > distance:
        return 0

    return 1 + (distance - k0) // 100


def main():
    rotations = load_input()
    position = 50
    zeros = 0

    # Part 1
    for rotation in rotations:
        position = dial(position, rotation)
        if position == 0:
            zeros += 1
    print("Part 1")
    print(f"The password is {zeros}")

    print()

    # Part 2
    position = 50
    zeros = 0
    for rotation in rotations:
        zeros += hit_zero(position, rotation)
        position = dial(position, rotation)

    print("Part 2")
    print(f"The password is {zeros}")


if __name__ == "__main__":
    main()
