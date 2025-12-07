from printing_department import load_diagram_2d, count_accessible_paper_rolls

def test_count_accessible_paper_rolls():
    diagram_txt = """
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
    diagram = load_diagram_2d(diagram_txt)

    accessible_marked_diagram_txt = """
                ..xx.xx@x.
                x@@.@.@.@@
                @@@@@.x.@@
                @.@@@@..@.
                x@.@@@@.@x
                .@@@@@@@.@
                .@.@.@.@@@
                x.@@@.@@@@
                .@@@@@@@@.
                x.x.@@@.x.
    """
    accessible_marked_diagram = load_diagram_2d(accessible_marked_diagram_txt)
    accessible_rolls = 0

    for line in accessible_marked_diagram:
        for char in line:
            if char == "x":
                accessible_rolls += 1
    
    assert count_accessible_paper_rolls(diagram) == accessible_rolls