"""Soldier and Bananas"""

def main():
    """Main function"""
    k, n, w = map(int, input().split())
    for i in range(w):
        n -= (i + 1) * k
    if (n > 0):
        print(0)
        return
    print(abs(n))
main()
