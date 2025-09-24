"""Nearly Lucky Number"""

def main():
    """Main function"""
    n = input()
    count = sum(1 for c in n if c in '47')
    print("YES") if count == 4 or count == 7 else print("NO")

main()
