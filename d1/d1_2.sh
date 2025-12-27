#!/usr/bin/env bash
# starting dial position
dial_position=50
zero_count=0
click_count=0


while read -r line; do
	printf "%s\t%3d => " $line $dial_position
	# get change in positon
	move_direction=${line:0:1}
	move_distance=${line:1}

	if [[ $move_direction == "L" ]]; then
		distance_to_zero=$((dial_position))
		signed_move_distance="-$move_distance"
	else
		distance_to_zero=$((100-dial_position))
		signed_move_distance=$move_distance
	fi
	
	if [[ $dial_position -eq 0 && $move_direction != $last_move_direction ]]; then
		click_count=$((click_count + move_distance/100))
	else
		click_count=$((click_count + (move_distance-distance_to_zero+100)/100))
	fi

	dial_position=$(((dial_position+signed_move_distance+100)%100))
	last_move_direction=$move_direction
	
	if [[ $dial_position -eq 0 ]]; then
		((zero_count++))
	fi
	#echo "$line\tposition:$dial_position\tzero_count:$zero_count\tclick_count:$click_count"
	printf "%3d\tzc:%3d\t\tcc:%3d\n" $dial_position $zero_count $click_count
#done < day1_my_input.txt
done < day1_sample_input.txt

