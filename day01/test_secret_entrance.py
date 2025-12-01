import random

from secret_entrance import dial
from secret_entrance import hit_zero
from secret_entrance import hit_zero_brute_force

# Following these rotations would cause the dial to move as follows:
# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32.


def test_dial():
    assert dial(50, "L68") == 82
    assert dial(82, "L30") == 52
    assert dial(52, "R48") == 0
    assert dial(0, "L5") == 95
    assert dial(95, "R60") == 55
    assert dial(55, "L55") == 0
    assert dial(0, "L1") == 99
    assert dial(99, "L99") == 0
    assert dial(0, "R14") == 14
    assert dial(14, "L82") == 32



def test_hit_zero():
    for _ in range(10000):
        pos = random.randint(0, 99)
        dist = random.randint(1, 2000)
        direction = random.choice("LR")
        rot = f"{direction}{dist}"
        assert hit_zero(pos, rot) == hit_zero_brute_force(pos, rot)