#!/usr/bin/env python
import sys

class Junction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Link:
    def __init__(self, junction1, junction2):
        self.junctions = [junction1, junction2]

    @property
    def distance(self):
        return  ((self.junctions[0].x - self.junctions[1].x)**2 +
                (self.junctions[0].y - self.junctions[1].y)**2 +
                (self.junctions[0].z - self.junctions[1].z)**2)**(1/2)

class Circuit:
    def __init__(self):
        self.links = set()
        self.junctions = set()

    def add_link(self, link):
        self.links.add(link)
        self.junctions.update(link.junctions)

    def merge(self, other):
        self.links.update(other.links)
        self.junctions.update(other.junctions)

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
    for circuit in circuits:
        if any([junction in circuit.junctions for junction in link.junctions]):
            if found_circuit:# if in 2, add to 1st merge the 2nd circuit, remove the 2nd from list
                found_circuit.merge(circuit)
                circuit.add_link(link)
                circuits.remove(circuit)
            else:# if in 1, add to the circuit
                circuit.add_link(link)
                found_circuit = circuit
    if not found_circuit:# if none create a new circuit
        circuits.append(Circuit())
        circuits[-1].add_link(link)
    if all_junctions_connected(junctions, circuits):
        break

result = link.junctions[0].x * link.junctions[1].x
print(f"Result is {result:.0f}")


