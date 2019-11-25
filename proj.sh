rm -f abc.txt
x=$(iostat -dxm sda)
y=$(nicstat -n)
z=$(mpstat)
w=$(free)

echo "disk read" >>abc.txt
echo "$x" | cut -d' ' -f48 >>abc.txt
echo "disk write" >>abc.txt
echo "$x" | cut -d' ' -f50 >>abc.txt
echo "%util" >>abc.txt
echo "$y" |cut -d' '  -f32 >>abc.txt
echo "%idle" >>abc.txt
echo "$z" |cut -d' '  -f43 >>abc.txt
echo "freeMem" >>abc.txt
echo "$w" | grep Mem | awk '{print $3/$2 * 100.0}' >>abc.txt

for one_var in $x; do

        #printf " '$xa'  '$one_var' \n"
        xa=$((xa+1))
done
x=$(echo abc.txt)
awk 'NF' $x > ab.txt
rm abc.txt

