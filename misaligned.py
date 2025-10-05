def get_color_pairs():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    pairs=[]
    pair_number=1
    for i in enumerate(major_colors):
        for j in enumerate(minor_colors):
            pairs.append((pair_number,i,j))
            pair_number+=1
    return pairs

def print_color_map():
    pairs=get_color_pairs()
    for number,major,minor in pairs:
        print(f"{number} | {major} | {minor}")
    return len(pairs)
result = print_color_map()

def test_get_color_pairs_length():
    """Should produce exactly 25 pairs."""
    pairs = get_color_pairs()
    assert len(pairs) == 25, "Expected 25 color pairs"

def test_color_pair_format():
    """Each pair should have proper color names, not tuples."""
    pairs = get_color_pairs()
    # The major and minor colors should be strings, not tuples
    for number, major, minor in pairs:
        assert isinstance(major, str), f"Major color is not a string: {major}"
        assert isinstance(minor, str), f"Minor color is not a string: {minor}"

def test_print_output_format(capsys):
    """Output should not contain parentheses or commas from tuples."""
    print_color_map()
    captured = capsys.readouterr().out
    assert '(' not in captured, "Output contains tuple representation"
    assert ',' not in captured, "Output contains tuple commas"
    assert "White" in captured and "Blue" in captured, "Expected colors not found"
test_get_color_pairs_length()
test_color_pair_format()
test_print_output_format()
