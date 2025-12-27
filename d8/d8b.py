import sys

class Junction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:4.0f},{self.y:4.0f},{self.z:4.0f})"

    def distance_to(self, other):
        return ((other.x - self.x)**2 + 
                (other.y - self.y)**2 +
                (other.z - self.z)**2)**(1/2)

class Link:
    def __init__(self, junction1, junction2):
        self.junctions = [junction1, junction2]

    def __str__(self):
        return f"({self.junctions[0].x:.0f},{self.junctions[0].y:.0f},{self.junctions[0].z:.0f})->({self.junctions[1].x:.0f},{self.junctions[1].y:.0f},{self.junctions[1].z:.0f})"

    @property
    def distance(self):
        return  ((self.junctions[0].x - self.junctions[1].x)**2 +
                (self.junctions[0].y - self.junctions[1].y)**2 +
                (self.junctions[0].z - self.junctions[1].z)**2)**(1/2)

class Circuit:
    def __init__(self):
        self.links = []
        self.junctions = []

    def __str__(self):
        return f"Circuit containing {len(self.links)} links and {len(self.junctions)} junctions"

    @property
    def size(self):
        return len(self.junctions)

    def add_link(self, link):
        self.links.append(link)
        for junction in link.junctions:
            if junction not in self.junctions:
                self.junctions.append(junction)

    def merge(self, other):
        self.links += other.links
        for junction in other.junctions:
            if junction not in self.junctions:
                self.junctions.append(junction)

def all_junctions_connected(junctions, circuits):
    return all( [
            any([junction in circuit.junctions for circuit in circuits])
            for junction in junctions ] )

junctions = []
for line in sys.stdin:
    x,y,z = line.strip().split(',')
    junctions.append(Junction(float(x), float(y), float(z)))

links = [Link(j1,j2) for i,j1 in enumerate(junctions) for j,j2 in enumerate(junctions[i+1:], start=i+1)]
links.sort(key = lambda x: x.distance)

circuits = []
for link in links:
    found_circuit = False
    # check if either junction is in any circuit
    # if none create a new circuit
    # if in 1, add to the circuit
    # if in 2, add to 1st merge the 2nd circuit, remove the 2nd from list
    for circuit in circuits:
        if any([junction in circuit.junctions for junction in link.junctions]):
            if found_circuit:
                found_circuit.merge(circuit)
                circuit.add_link(link)
                circuits.remove(circuit)
            else:
                circuit.add_link(link)
                found_circuit = circuit
    if not found_circuit:
        circuits.append(Circuit())
        circuits[-1].add_link(link)
    if all_junctions_connected(junctions, circuits):
        print("Yay!")
        break

# circuits.sort(key = lambda x: x.size, reverse=True)
if len(circuits) > 1:
    print("WTF happened?")

print(link)
result = link.junctions[0].x * link.junctions[1].x
print(f"Result is {result:.0f}")


