"""Team"""

def main():
    """Main funtion"""
    cnt = 0
    for _ in range(int(input())):
        c: list = input().split()
        if c.count('1') >= 2: cnt += 1
    print(cnt)

main()
