"""Football"""

def main():
    """Main function"""
    s: str = str(input())
    print("YES") if "1" * 7 in s or "0" * 7 in s else print("NO")
main()
