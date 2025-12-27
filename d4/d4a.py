import sys
MAX_LINE_LENGTH = 10
dummy_line = '.' * MAX_LINE_LENGTH

def get_neighbors(prev_line, line, next_line, too_many_neighbors=4):
    marked_line = line
    num_rolls = 0
    for n, char in enumerate(line):
        num_neighbors = 0
        if char == '.':
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

markedmap = []
originalmap = []
num_accessible_rolls = 0

# set up first line
prev_line = dummy_line
line = sys.stdin.readline().strip()

# loop thru middle lines
for next_line in sys.stdin:
    next_line = next_line.strip()
    originalmap.append(line)
    num_rolls, marked_line = get_neighbors(prev_line, line, next_line, 4)
    markedmap.append(marked_line)
    num_accessible_rolls += num_rolls
    prev_line, line = line, next_line
else: # last line
    next_line = dummy_line
    originalmap.append(line)
    num_rolls, marked_line = get_neighbors(prev_line, line, next_line, 4)
    markedmap.append(marked_line)
    num_accessible_rolls += num_rolls
print()
print('\n'.join(originalmap))
print()
print('\n'.join(markedmap))
print()
print(f"Num accessible rolls = {num_accessible_rolls}")