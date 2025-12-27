#!/usr/bin/env bash

find_max_index() {
	local nums=$1 start=$2 end=$3
	local max=-1 maxi=0
	local val i
	for (( i=$start; i<=$end; i++ )); do
		val=${nums:$i:1}
		if [[ $val > $max ]]; then
		       max=$val
		       maxi=$i
		fi
	done
	echo "$maxi"
}

get_joltage() {
	local num_digits=$2 bank=$1
	local len=${#bank}
	local banki i mini=0 maxi joltage=0
	for (( i=0; i<$num_digits; i++ )); do
		maxi=$(( len - num_digits + i ))
		banki=$( find_max_index $bank $mini $maxi )
		mini=$(( banki + 1 ))
		(( joltage+=${bank:banki:1}*10**(num_digits-i-1) ))
	done
	echo "$joltage"
}

num_digits=${1:-2} # take from command line, default=2
jolts=0
while read -r bank; do
	joltage=$( get_joltage $bank $num_digits ) 
	((jolts+=joltage))
done
echo "$jolts jolts"
