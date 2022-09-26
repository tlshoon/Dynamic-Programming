# 피보나치 함수 소스코드 (동일함 함수 반복 호출)
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# print(fibo(4))

# 피보나치 수열 소스코드(재귀적)
# d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
#
# def fibo(x):  # 탑다운 다이나믹 프로그래밍
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:  # 이미 계산한 적 있는 문제라면 그대로 반환
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2) # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#     return d[x]
#
# print(fibo(99))

# 호출되는 함수 확인
# d = [0] * 100
#
# def fibo(x):
#     print('f('+str(x)+')', end=' ')
#     if x == 1 or x == 2\\\\\\\\\\\\\\
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
# fibo(6)

# 피보나치 수열 소스코드(반복적)
# d = [0] * 100  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
#
# d[1] = 1
# d[2] = 1
# n = 99
#
# for i in range(3, n+1): # 보텀업 다이나믹 프로그래밍
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])

