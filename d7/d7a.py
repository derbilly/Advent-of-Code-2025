import sys

def display_manifold(manifold):
    width = len(manifold[0])
    print('|' + '-'*(width + 4) + '|')
    print('|' + ' '*(width + 4) + '|')
    for line in manifold:
        print(f"|  {line}  |")
    print('|' + ' '*(width + 4) + '|')
    print('|' + '-'*(width + 4) + '|')

def find_sources(line):
    return [i for i, char in enumerate(line) if char=='S' or char=='|']

manifold=[]
for line in sys.stdin:
    manifold.append(line.strip())

display_manifold(manifold)


num_splits = 0
sources = []
for line in manifold:
    for source in sources:
        if line[source] == '^':
            line = line[:source-1] + '|^|' + line[source+2:]
            num_splits += 1
        else:
            line = line[:source] + '|' + line[source+1:]
    sources = find_sources(line)
    print(line)
print(f"Total splits: {num_splits}")
