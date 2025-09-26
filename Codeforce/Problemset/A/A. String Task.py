"""String Task"""

def main():
    """Main function"""
    for t in str(input()):
        if t.lower() not in "aoyeui":
            print('.' + t.lower(), end="")
    print('\n')
main()
