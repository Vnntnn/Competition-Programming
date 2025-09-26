"""A. Way Too Long Words"""

def main():
    """Main function"""
    for _ in range(int(input())):
        t = str(input())
        if (len(t) <= 10):
            print(t)
            continue
        print(t[:1] + str(len(t[1:-1])) + t[-1])

main()
