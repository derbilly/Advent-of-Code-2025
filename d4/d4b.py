import sys

def get_neighbors(prev_line, line, next_line, too_many_neighbors=4):
    marked_line = line
    num_rolls = 0
    for n, char in enumerate(line):
        num_neighbors = 0
        if char != '@':
            continue
        if n==0:
            num_neighbors += ( prev_line[:n+2].count('@')
                              + line[1].count('@')
                              + next_line[:n+2].count('@') )
        elif n == len(line) - 1:
            num_neighbors += ( prev_line[n-1:n+1].count('@')
                              + line[n-1:n+1].count('@') - 1
                              + next_line[n-1:n+1].count('@') )
        else:
            num_neighbors += ( prev_line[n-1:n+2].count('@')
                              + line[n-1:n+2].count('@') - 1
                              + next_line[n-1:n+2].count('@') )
        if num_neighbors < too_many_neighbors:
            num_rolls += 1
            marked_line = marked_line[:n] + 'x' + marked_line[n+1:]
    return num_rolls, marked_line

def remove_rolls(current_map):
    new_map = []
    num_rolls_removed = 0
    # set up first line
    prev_line = dummy_line
    line = current_map[0]
    # loop thru middle lines
    for next_line in current_map[1:]:
        removable_rolls, marked_line = get_neighbors(prev_line, line, next_line, 4)
        new_map.append(marked_line)
        num_rolls_removed += removable_rolls
        prev_line, line = line, next_line
    else: # last line
        next_line = dummy_line
        removable_rolls, marked_line = get_neighbors(prev_line, line, next_line, 4)
        new_map.append(marked_line)
        num_rolls_removed += removable_rolls
    return num_rolls_removed, new_map

floor_map = [line.strip() for line in sys.stdin.readlines()]
MAX_LINE_LENGTH = max([len(line) for line in floor_map])
dummy_line = '.' * MAX_LINE_LENGTH
total_removed_rolls = 0
print('\n'.join(floor_map))
print()
marked_map = floor_map
while True:
    num_rolls_removed, marked_map = remove_rolls(marked_map)
    if num_rolls_removed == 0:
        break
    total_removed_rolls += num_rolls_removed
    print('\n'.join(marked_map))

print(f"Total rolls removed = {total_removed_rolls}")