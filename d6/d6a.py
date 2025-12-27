import sys

operand_sets = []
for line in sys.stdin:
    operand_sets.append(line.strip().split())
operations = operand_sets.pop()
#print(operand_sets)
#print(operations)
calculations = operand_sets[0]
for operands in operand_sets[1:]:
    calculations = [ calculation + operation + operand for calculation, operation, operand in zip(calculations, operations, operands) ]
#print('\n'.join(calculations))
results = [ eval(calculation) for calculation in calculations ]
#print(results)
print(f"Sum of calculations: {sum(results)}")
