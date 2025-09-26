"""Anton and Danik"""

def main():
    """Main function"""
    _: int = int(input())
    s: str = str(input())

    print("Danik") if s.upper().count('D') > s.upper().count('A') else \
    print("Anton") if s.upper().count('A') > s.upper().count('D') else print("Friendship")
main()
