import sys

joltage_sum = 0

def get_joltage(bank):

    # find max digit
    # find index of max digit
    # print(f"<{bank}>")
    first_digit_index = bank.find(max(bank))
    # check that it is not the last digit
    if (first_digit_index == len(bank)-1):
        first_digit_index = bank[:-1].find(max(bank[:-1]))
    # print(first_digit_index)
    # find max of remaining 
    second_digit_index = bank[first_digit_index+1:].find(max(bank[first_digit_index+1:]))+first_digit_index+1
    # print(second_digit_index)
    return 10*int(bank[first_digit_index]) + int(bank[second_digit_index])

for line in sys.stdin:
    line = line.strip()
    joltage = get_joltage(line)
    # print(joltage)
    joltage_sum += joltage
print(joltage_sum)
