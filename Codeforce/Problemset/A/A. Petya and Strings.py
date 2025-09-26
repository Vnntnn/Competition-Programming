"""Petya and Strings"""

def main():
    """Main function"""
    a = str(input()).lower()
    b = str(input()).lower()
    print(-1) if a < b else print(1) if a > b else print(0)
main()
