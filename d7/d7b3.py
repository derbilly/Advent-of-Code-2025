import sys

manifold=[]
for line in sys.stdin:
    manifold.append(line.strip())

timelines = 1
sources = [int(char == 'S') for char in manifold[0]]
for n in range(1, len(manifold)):
    new_sources = [0]*len(sources)
    for j, num in enumerate(sources):
        if num>0 and manifold[n][j] == '^':
            new_sources[j-1] += num
            new_sources[j+1] += num
            timelines += num
        else:
            new_sources[j] += num
    sources = new_sources

print(f"Total timelines: {timelines}")
