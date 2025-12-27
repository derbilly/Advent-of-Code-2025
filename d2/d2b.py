#/usr/bin/env python
import sys
import re
invalid_count=0
invalid_sum=0
search_ranges = sys.stdin.read().strip().split(',')
search_ranges = [tuple([int(val) for val in x.split('-')]) for x in search_ranges]

def is_code_invalid(code):
        code = str(code)
        for repeated_characters in range(1, len(code)//2+1):
            repeats = len(code)//repeated_characters
            if code == code[:repeated_characters]*repeats:
                return True
        return False

for start, stop in search_ranges:
    #print(f'searching range {start}-{stop}.')
    for code in range(start, stop + 1):
        #if bool(re.fullmatch(r'^(.+)\1+$', str(code))):
        if is_code_invalid(code):
            invalid_count += 1
            invalid_sum += code
            #print(f'code {code} is invalid!')
print(f'Num invalid codes: {invalid_count}')
print(f'Sum invalid codes: {invalid_sum}')
