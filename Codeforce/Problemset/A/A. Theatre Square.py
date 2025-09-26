"""Theatre Square"""

import math

def main():
    """Main function"""
    m, n, a = map(int, input().split())
    print(math.ceil(m / a) * math.ceil(n / a))

main()
