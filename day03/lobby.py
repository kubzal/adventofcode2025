# Description: https://adventofcode.com/2025/day/3

import os
import requests

from dotenv import load_dotenv

from icecream import ic


def load_input(
    url="https://adventofcode.com/2025/day/3/input", filename="day03_input.txt"
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
def largest_possible_joltage(bank: str):
    bank = str(bank)

    batteries_dict = dict()
    for idx, battery in enumerate(bank):
        battery = int(battery)
        if battery in batteries_dict.keys():
            batteries_dict[battery].append(idx)
        else:
            batteries_dict[battery] = [idx]

    available_batteries_desc = sorted(batteries_dict.keys(), reverse=True)

    for battery in available_batteries_desc:
        idx_first = batteries_dict[battery][0]
        if idx_first != len(bank) - 1:
            break

    for battery in available_batteries_desc:
        idxs_gt_first = [x for x in batteries_dict[battery] if x > idx_first]
        idx_second = min(idxs_gt_first) if len(idxs_gt_first) > 0 else -1
        if idx_second > idx_first:
            break

    return int(bank[idx_first] + bank[idx_second])


# Part 2
def largest_possible_joltage_12(bank: str):
    bank = str(bank)

    batteries_dict = dict()
    for idx, battery in enumerate(bank):
        battery = int(battery)
        if battery in batteries_dict.keys():
            batteries_dict[battery].append(idx)
        else:
            batteries_dict[battery] = [idx]

    batteries_order = list()
    while len(batteries_order) < 12:
        available_batteries_desc = sorted(batteries_dict.keys(), reverse=True)
        for battery in available_batteries_desc:
            if batteries_dict[battery][0] <= (len(bank) - (12 - len(batteries_order))):
                if len(batteries_order) == 0:
                    batteries_order.append(batteries_dict[battery].pop(0))
                    if len(batteries_dict[battery]) == 0:
                        batteries_dict.pop(battery, None)
                else:
                    if batteries_dict[battery][0] > batteries_order[-1]:
                        batteries_order.append(batteries_dict[battery].pop(0))
                        if len(batteries_dict[battery]) == 0:
                            batteries_dict.pop(battery, None)
                    else:
                        batteries_dict[battery].pop(0)
                        if len(batteries_dict[battery]) == 0:
                            batteries_dict.pop(battery, None)
                break

    return int("".join([bank[idx] for idx in batteries_order]))


def main():
    banks = load_input()

    total_joltage = 0
    for bank in banks:
        joltage = largest_possible_joltage(bank)
        total_joltage += joltage

    print("Part 1: Total joltage:", total_joltage)

    # Part 2
    total_joltage = 0
    for bank in banks:
        joltage = largest_possible_joltage_12(bank)
        total_joltage += joltage

    print("Part 2: Total joltage:", total_joltage)


if __name__ == "__main__":
    main()
