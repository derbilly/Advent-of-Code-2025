#!/usr/bin/env bash
# starting dial position
dial_position=50
zero_count=0
update_position() {
	direction=${line:0:1}
	distance=${line:1}
	if [[ $direction == "L" ]]; then
		distance="-$distance"
	fi
	dial_position=$(((dial_position+distance+100)%100))
}


while read -r line; do
	echo "$line"
	update_position
	echo $dial_position
	if [[ $dial_position -eq 0 ]]; then
		((zero_count++))
	fi
done < day1_my_input.txt

echo $zero_count
