from lobby import largest_possible_joltage, largest_possible_joltage_12


def test_largest_possible_joltage():
    assert largest_possible_joltage("987654321111111") == 98
    assert largest_possible_joltage("811111111111119") == 89
    assert largest_possible_joltage("234234234234278") == 78
    assert largest_possible_joltage("818181911112111") == 92

def test_largest_possible_joltage_12():
    assert largest_possible_joltage_12("987654321111111") == 987654321111
    assert largest_possible_joltage_12("811111111111119") == 811111111119
    assert largest_possible_joltage_12("234234234234278") == 434234234278
    assert largest_possible_joltage_12("818181911112111") == 888911112111