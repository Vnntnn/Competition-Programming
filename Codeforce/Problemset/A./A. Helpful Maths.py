"""Helpful Maths"""

def main():
    """Main function"""
    print('+'.join(map(str, sorted(map(int, input().split('+'))))))
main()