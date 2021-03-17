#최대 공약수 구하는 함수
#유클리드 호제법
#a>b이고, r이 a%b 일 때,
#a, b 의 최대공약수는 b와 r의 최대공약수와 같다.


def gcd(a, b):
    if (a % b) == 0:
        return b
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a, b))

#a가 b보다 작은 수를 넣어도 이 함수는 돌아감
