"""Stones on the Table"""

def main():
    """Main function"""
    n: int = int(input())
    stones: list = list(map(str, input()))
    cnt: int = 0
    for i in range(n):
        if (i < n - 1 and stones[i] == stones[i + 1]):
            cnt += 1
    print(cnt)
main()
