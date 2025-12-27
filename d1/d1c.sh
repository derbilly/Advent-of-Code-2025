#!/usr/bin/env bash
# starting dial position
dial_position=50
zero_count=0
click_count=0


while read -r line; do
	printf "%5s %2d>" $line $dial_position
	# get change in positon
	move_direction=${line:0:1}
	move_distance=${line:1}

		
	if [[ $move_direction == "L" ]]; then
		distance_to_zero=$((dial_position))
		move_sign=-1
		#signed_move_distance="-$move_distance"
	else
		distance_to_zero=$((100-dial_position))
		#signed_move_distance=$move_distance
		move_sign=1
	fi
	if [[ $dial_position -eq 0 ]]; then
		distance_to_zero=100
	fi
	click_count=$((click_count + move_distance/100))
	if [[ $((move_distance%100)) -ge $distance_to_zero ]]; then
		((click_count++))
	fi
	
	dial_position=$(((dial_position+move_sign*(move_distance%100)+100)%100))
	
	if [[ $dial_position -eq 0 ]]; then
		((zero_count++))
	fi
	printf "%2d zc:%4d cc:%4d\n" $dial_position $zero_count $click_count
done
#done < day1_my_input.txt
# done < day1_sample_input.txt

