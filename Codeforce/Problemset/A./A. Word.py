"""Word"""

def main():
    """Main function"""
    s: str = str(input())
    lcount, ucount = 0, 0
    lcount = sum(1 for c in s if 'a' <= c <= 'z'); ucount = len(s) - lcount

    if lcount < ucount:
        print(s.upper())
    else:
        print(s.lower())

main()
