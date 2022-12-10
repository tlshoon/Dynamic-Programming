# 피보나치 함수 소스코드 (동일함 함수 반복 호출)
# def fibo(x):
#     if x == 1 or x == 2:  # 멈추는 조건
#         return 1
#     return fibo(x-1) + fibo(x-2)
# print(fibo(4))

# 피보나치 수열 소스코드(재귀적), 탑다운
# d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
#
# def fibo(x):  # 탑다운 다이나믹 프로그래밍
#     if x == 1 or x == 2:  # 종료 조건
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

# 피보나치 수열 소스코드(반복적), 보텀업업# d = [0] * 100  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
#
# d[1] = 1
# d[2] = 1
# n = 99
#
# for i in range(3, n+1): # 보텀업 다이나믹 프로그래밍
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])

# LIS 최장 수열
# n = int(input())
# array = list(map(int,input().split()))
# dp = [0 for _ in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         if array[i] > array[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))

# 1로 만들기
# x = int(input())
#
# d = [0] * 30001
#
# for i in range(2,x+1):
#     # 현재의 수에서 1을 빼는 경우
#     d[i] = d[i-1] + 1   # 이전 값에 +1 하는 경우 (기본 정의)
#     # 현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i],d[i//2] + 1)  # 이전 값 + 1, 2로 나눈 값 (이전까지 세어진 값) + 1 중에 최소값
#     # 현재의 수가 3으로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     # 현재의 수가 5로 나누어 떨어지느 경우
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)
# print(d[x])

# 개미전사
# n = int(input())
# array = list(map(int,input().split()))
#
# d = [0] * 100 # 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
#
# d[0] = array[0]
# d[1] = max(array[0],array[1])
#
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2] + array[i])
#
# print(d[n-1])

# 바닥 공사
# n = int(input())
#
# d = [0] * 1001
#
# d[1] = 1
# d[2] = 3
#
# for i in range(3,n+1):
#     d[i] = (d[i-1] + 2 * d[i-2]) % 796796
# print(d[n])
