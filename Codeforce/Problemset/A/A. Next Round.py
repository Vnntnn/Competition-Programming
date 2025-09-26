"""A. Next Round"""

def main():
    """Main function"""
    n, k = map(int, input().split())
    cn = list(map(int, input().split()))
    adv = 0
    
    for i in range(n):
        if cn[i] >= cn[k - 1] and cn[i] > 0: 
            adv += 1

    print(adv)
main()
