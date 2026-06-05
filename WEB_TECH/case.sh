echo "Enter choice"
echo "1) List of files"
echo "2) List of users"
echo "3) Delete a file"
read ch

case $ch in
1) 
    echo "The list is:"
    ls
    ;;
2) 
    echo "The users are:"
    who
    ;;
3) 
    echo "Enter the file to be deleted:"
    read frame
    rm "$frame"
    ;;
*) 
    echo "Invalid choice"
    ;;
esac
