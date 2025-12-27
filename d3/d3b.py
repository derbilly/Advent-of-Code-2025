import sys

joltage_sum = 0

def get_joltage(bank):
    num_digits = 12
    digit_indices = []
    find_start = 0
    for digit_num in range(num_digits): # digits 0 to 12 l to r
        find_end = len(bank) - num_digits + digit_num + 1
        # print(f"searching digit{digit_num} in {bank} indices {find_start}-{find_end}, {bank[find_start:find_end]}")
        digit_indices.append(bank.find(max(bank[find_start:find_end]), find_start, find_end))
        find_start = digit_indices[-1] + 1
    print(f"{bank} {digit_indices}")
    joltage = 0
    for n, digit_index in enumerate(reversed(digit_indices)):
        joltage += int(bank[digit_index])*10**n
    return joltage

for line in sys.stdin:
    line = line.strip()
    print(line)
    joltage = get_joltage(line)
    print(f"{joltage} jolts")
    joltage_sum += joltage
print(f"{joltage_sum} jolts")