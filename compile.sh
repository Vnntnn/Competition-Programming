echo "Is your program C or C++?"
echo "1. C"
echo "2. C++"
read -r c

p="$1"

if [ "$c" = "1" ]; then
    gcc -o main "$p"
elif [ "$c" = "2" ]; then
    g++ -o main "$p"
fi
