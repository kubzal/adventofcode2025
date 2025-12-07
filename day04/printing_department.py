# Description: https://adventofcode.com/2025/day/4

import os
import requests

from dotenv import load_dotenv

from icecream import ic


def load_input(
    url="https://adventofcode.com/2025/day/4/input", filename="day04_input.txt"
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


def example_diagram() -> str:
    return """
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
    """


def print_diagram(diagram: list, i: int = -1, j: int = -1) -> None:
    if i >= 0 & j >= 0:
        for row_idx, line in enumerate(diagram):
            line_to_print = ""
            for col_idx, char in enumerate(line):
                if (row_idx == i) & (col_idx == j):
                    line_to_print += "X"
                else:
                    line_to_print += f"{char}"
            print(line_to_print)
    else:
        for line in diagram:
            print(line)


def load_diagram_2d(diagram_txt: str) -> list:
    diagram_txt = diagram_txt.replace(" ", "")
    return [line for line in diagram_txt.splitlines() if len(line) > 0]


def position_exist(diagram: list, i: int, j: int) -> bool:
    if (i >= 0) & (j >= 0):
        if i < len(diagram):
            if j < len(diagram[i]):
                return True
    return False


def is_paper_roll(diagram: list, i: int, j: int) -> bool:
    if diagram[i][j] == "@":
        return True
    else:
        return False


def position_exist_and_is_paper_roll(diagram: list, i: int, j: int) -> bool:
    if position_exist(diagram, i, j):
        if is_paper_roll(diagram, i, j):
            return True
    return False


def count_adjacent_paper_rolls(diagram: list, i: int, j: int) -> int:
    paper_rolls = 0
    # first row
    if position_exist_and_is_paper_roll(diagram, i - 1, j - 1):
        paper_rolls += 1
    if position_exist_and_is_paper_roll(diagram, i - 1, j):
        paper_rolls += 1
    if position_exist_and_is_paper_roll(diagram, i - 1, j + 1):
        paper_rolls += 1

    # second row
    if position_exist_and_is_paper_roll(diagram, i, j - 1):
        paper_rolls += 1
    if position_exist_and_is_paper_roll(diagram, i, j + 1):
        paper_rolls += 1

    # third row
    if position_exist_and_is_paper_roll(diagram, i + 1, j - 1):
        paper_rolls += 1
    if position_exist_and_is_paper_roll(diagram, i + 1, j):
        paper_rolls += 1
    if position_exist_and_is_paper_roll(diagram, i + 1, j + 1):
        paper_rolls += 1

    return paper_rolls

def is_accessible(diagram: list, i: int, j: int) -> bool:
    return count_adjacent_paper_rolls(diagram, i, j) < 4


def accessible_paper_rolls(diagram: list) -> tuple:
    cnt_accessible_paper_rolls = 0
    accessible_rolls_points = list()
    for i, line in enumerate(diagram):
        for j, char in enumerate(line):
            if char == "@":
                # check neighbours
                if is_accessible(diagram, i, j):
                    cnt_accessible_paper_rolls += 1
                    accessible_rolls_points.append((i, j))
    return cnt_accessible_paper_rolls, accessible_rolls_points

def remove_accessible_paper_rolls(diagram: list, accessible_paper_rolls_points: list) -> list:
    for i, j in accessible_paper_rolls_points:
        line = list(diagram[i])
        line[j] = "x"
        diagram[i] = "".join(line)
    return diagram

def main():
    diagram = load_input()
    
    iteration = 1
    total_accessible_rolls = 0

    while True:
        cnt_accessible_rolls, accessible_rolls_points = accessible_paper_rolls(diagram)
        total_accessible_rolls += cnt_accessible_rolls

        diagram = remove_accessible_paper_rolls(diagram, accessible_rolls_points) 

        if iteration == 1:
            print("Part 1:")

        if iteration == 2:
            print()
            print("Part 2:")
        
        print(f"[{iteration}] Accessible paper rolls: {cnt_accessible_rolls}")

        if cnt_accessible_rolls == 0:
            break
        
        iteration+= 1

    print()
    print(f"TOTAL Accessible paper rolls: {total_accessible_rolls}")

def test():
    diagram = load_diagram_2d(example_diagram())

    print_diagram(diagram)

    cnt_accessible_paper_rolls, accessible_paper_rolls_points = accessible_paper_rolls(diagram)
    print()
    print("Accessible paper rools:", cnt_accessible_paper_rolls)

    diagram = remove_accessible_paper_rolls(diagram, cnt_accessible_paper_rolls)
    print()
    print("Diagram after removing accessible paper rolls:")
    print_diagram(diagram)


if __name__ == "__main__":
    main()
    # test()