"""Bear and Big Brother"""

def main():
    """Main function"""
    bears = list(map(int, input().split()))
    c: int = 0
    while (bears[0] <= bears[1]):
        c += 1
        bears[0] *= 3
        bears[1] *= 2

    print(c)
main()