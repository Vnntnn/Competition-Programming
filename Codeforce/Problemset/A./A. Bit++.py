"""Bit++"""

def main():
    """Main function"""
    n = 0
    for _ in range(int(input())): n = n + 1 if "++" in str(input()) else n - 1
    print(n)

main()
