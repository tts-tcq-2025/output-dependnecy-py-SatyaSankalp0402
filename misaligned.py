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
    pairs = get_color_pairs()
    assert len(pairs) == 25, "Expected 25 color pairs"

def test_color_pair_format():
    pairs = get_color_pairs()
    for number, major, minor in pairs:
        assert isinstance(major, str), f"Major color is not a string: {major}"
        assert isinstance(minor, str), f"Minor color is not a string: {minor}"

test_get_color_pairs_length()
test_color_pair_format()
