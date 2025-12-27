#!/usr/bin/env bash
invalid_count=0
invalid_sum=0

is_code_invalid() {
	local mycode=$1
	local len=${#mycode}

	for (( num_chars=1; num_chars<=len/2; num_chars++ )); do
		# check if code is evenly divisible by that number of characters
#		if  (( $len % $num_chars != 0 )); then
#			continue
#		fi
		# generate testcode
		local repeats=$(( len/num_chars ))
		local testcode=""
		local codeblock=${mycode:0:num_chars}
		for (( n=0; n<repeats; n++ )); do
			testcode="$testcode$codeblock"
		done
		#printf "%s = %s?\n" $mycode $testcode

		if [[ $code == $testcode ]]; then
			return 0
		fi
	done
	return 1
}

IFS=',' read -r -a ranges

for range in "${ranges[@]}"; do
	IFS='-' read -r start stop <<< "$range"
	#start=${range%-*}
	#stop=${range#*-}
	#printf "checking range, %d-%d ...\n" $start $stop
	printf "%d-%d " $start $stop
	for (( code=start; code<=stop; code++ )); do
		# echo $code
		if is_code_invalid $code; then
			#echo "$code is invalid"
			printf "%d " $code
			((invalid_count++))
			((invalid_sum += code))
		fi
	done
	printf "\n"
done
printf "%d invalid codes summing to %d.\n" $invalid_count $invalid_sum
# echo "num invalid codes: $invalid_count"
# echo "sum of invalid codes: $invalid_sum"
