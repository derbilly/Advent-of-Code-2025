import sys

manifold=[]
for line in sys.stdin:
    manifold.append(line.strip())

timelines = 1
sources = [manifold[0].find('S')]
for n in range(1, len(manifold)):
    print(f"{n} {len(sources)}")
    new_sources = []
    for source in sources:
        if manifold[n][source] == '^':
            new_sources += [source-1, source+1]
            timelines += 1
        else:
            new_sources += [source]
    sources = new_sources

print(f"Total timelines: {timelines}")
