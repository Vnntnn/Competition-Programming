"""Wrong Subtraction"""

def main():
    """Main function"""
    l: list[int] = list(map(int, str(input()).split()))
    while l[1] != 0:
        if not l[0] % 10:
            l[0] //= 10
        else:
            l[0] -= 1
        l[1] -= 1
    print(int(l[0]))
main()
