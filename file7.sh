echo "enter file name"
read file
[ -w $file ] && W="write = yes " || W="Write = no "
[ -x $file ] && X="execute = yes" || X=" execute = no"
[ -r $file ] && R="read = yes" || R=" read = no"
echo "$W"
echo "$R"
echo "$X"


