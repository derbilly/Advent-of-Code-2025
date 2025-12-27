import sys

problem_input = sys.stdin.read().splitlines()
operation_input = [''.join(row) for row in zip(*problem_input)]

operation_str = ''
for item in operation_input:
    if item.endswith('*') or item.endswith('+'):
        operation = item[-1]
        operation_str += item[:-1]
    elif item.isspace():
        operation_str += '+'
    else:
        operation_str += operation + item

print(f"Sum of calculations: {eval(operation_str)}")

