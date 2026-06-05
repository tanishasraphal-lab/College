ch="y"
while [ "$ch" = "y" ]
do
    echo "Enter a number"
    read number
    fact=1
    while [ "$number" -gt 1 ]
    do
        fact=$((fact * number))
        number=$((number - 1))
    done
    echo "Factorial is $fact"
    echo "Do you want to continue (y/n)?"
    read ch
done
