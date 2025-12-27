<my.d2a tr ,- '\n ' |xargs -L1 seq |grep -E '^(.+)\1+$' |paste -sd+ - |bc
