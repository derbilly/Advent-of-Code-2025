import sys

def get_timelines(source, manifold):
    lines_left = len(manifold)
    if lines_left == 1:
        if manifold[0][source] == '^':
            return 2
        else:
            return 1
    else:
        if manifold[0][source] == '^':
            return get_timelines(source-1, manifold[1:]) + get_timelines(source+1, manifold[1:])
        else:
            return get_timelines(source, manifold[1:])

manifold=[]
for line in sys.stdin:
    manifold.append(line.strip())

source = manifold[0].find('S')
timelines = get_timelines(source, manifold[1:])
print(f"Total timelines: {timelines}")
