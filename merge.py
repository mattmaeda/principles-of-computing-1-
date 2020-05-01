"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    compressed_line = []
    previous_tile = None
    for tile in filter(lambda tile: tile != 0, line):
        if not previous_tile:
            previous_tile = tile
        else:
            if tile == previous_tile:
                compressed_line.append(tile + previous_tile)
                previous_tile = None
            else:
                compressed_line.append(previous_tile)
                previous_tile = tile
    if previous_tile is not None:
        compressed_line.append(previous_tile)

    compressed_line += [0] * (len(line) - len(compressed_line))

    return compressed_line

if __name__ == "__main__":
    assert(merge([]) == [])
    assert(merge([1,1]) == [2,0])
    assert(merge([1,1,2]) == [2,2,0])
    assert(merge([2,1,1,2]) == [2,2,2,0])
    assert(merge([2,2,1,1]) == [4,2,0,0])
    assert(merge([1,2,3,4]) == [1,2,3,4])
    assert(merge([8,8]) == [16,0])
    assert(merge([8,0,8]) == [16,0,0])
