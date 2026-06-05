myfunc()
{
    echo "I was called as $@"
    x=2
}

echo "Script was called with the $@"
x=1
echo "x is $x"
myfunc 1 2 3
echo "x is $x"
