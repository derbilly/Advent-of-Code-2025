#/usr/bin/env python
import sys
invalid_count=0
invalid_sum=0
search_ranges = sys.stdin.read().strip().split(',')
search_ranges = [tuple([int(val) for val in x.split('-')]) for x in search_ranges]
for start, stop in search_ranges:
    for num in range(start, stop + 1):
        numstr = str(num)
        if (len(numstr)%2)==0 and (numstr[:len(numstr)//2] == numstr[len(numstr)//2:]):
            invalid_count += 1
            invalid_sum += num
            # print(numstr)
print(f'Num invalid codes: {invalid_count}')
print(f'Sum invalid codes: {invalid_sum}')
