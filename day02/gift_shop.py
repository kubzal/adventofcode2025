# Description: https://adventofcode.com/2025/day/2

import os
import requests

from dotenv import load_dotenv


def load_input(
    url="https://adventofcode.com/2025/day/2/input", filename="day02_input.txt"
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


# Part 1
def invalid_id(id: int) -> bool:
    id = str(id)
    if len(id) % 2 != 0:
        return False

    sequence_len = len(id) // 2
    id_to_compare = id[0:sequence_len] * 2
    if id == id_to_compare:
        return True
    else:
        return False


# Part 2
def invalid_id_at_leat_twice(id: int) -> bool:
    id = str(id)
    max_sequence_len = len(id) // 2

    for sequence_len in range(1, max_sequence_len + 1):
        if len(id) % sequence_len != 0:
            continue

        number_of_sequences_in_id = int(len(id) // sequence_len)
        id_to_compare = id[0:sequence_len] * number_of_sequences_in_id
        if id == id_to_compare:
            return True
    return False


def main():
    id_ranges = [tuple(id_range.split("-")) for id_range in load_input()[0].split(",")]

    # Part 1
    invalid_ids = 0
    for min_val, max_val in id_ranges:
        iteration_invalid_ids = 0
        for id in range(int(min_val), int(max_val) + 1):
            if invalid_id(id):
                iteration_invalid_ids += int(id)
        invalid_ids += iteration_invalid_ids

    print("Part 1: Invalid IDs sum: ", invalid_ids)

    # Part 2
    invalid_ids = 0
    for min_val, max_val in id_ranges:
        iteration_invalid_ids = 0
        for id in range(int(min_val), int(max_val) + 1):
            if invalid_id_at_leat_twice(id):
                iteration_invalid_ids += int(id)
        invalid_ids += iteration_invalid_ids

    print("Part 2: Invalid IDs sum: ", invalid_ids)


if __name__ == "__main__":
    main()
