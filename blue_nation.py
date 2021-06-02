#A oi

# ans = 0
# for i in range(1,2021):
#     if str(i).count("2") != 0:
#         ans += 1
# print(ans)

#B oi
# ans = 0
# for i in range(1,2021):
#     for j in range(2,i):
#         if i % j == 0 :
#             ans += 1
#             break
# print(ans)

#C  大数据量
# # p[i]表示第i个数分解时一共用了多少个
# p = [0 for i in range(101)]
# # 对2-100每一个数字进行质因数分解
# for number in range(2, 101):
#     # 当前要分解的数字
#     now_number = number
#     # 质因数分解
#     j = 1
#     while j <= (now_number // j):
#         j += 1
#         # 求用了多少个这个数字
#         while now_number % j == 0:
#             p[j] += 1
#             now_number //= j
#     # 最后分解完剩下一个数字
#     if now_number > 1:
#         p[now_number] += 1
#
# # 根据公式求约数个数
# ans = 1
# for i in range(2, 101):
#     if p[i] != 0:
#         ans *= (p[i] + 1)
#
# print(ans)

#D  DP
# s = ''
# with open('blue.txt','r') as f:
#     s = f.readline()
# s = s[:-1]
# length = len(s)
# dp = [1] * length
# ans = 0
# for i in range(1,length):
#     for j in range(i):
#         if s[i] > s[j]:
#             dp[i] += dp[j]
#         if s[i] == s[j]:
#             dp[i] -= dp[j]
# for i in dp:
#     ans += i
# print(ans)

#E dfs bfs
# # 依次将数字1放入16个格子中
# # 利用深度搜索找到可能的方案
# # 题目中90度的意思是只能从当前位置
# # 向上，下，左，右四个方向进行搜索
# # 最终答案
# ans = 0
# # 方格
# grid = [[0] * 4 for i in range(4)]
# # 状态标记,当前位置是否已经填充数字
# visit = [[False] * 4 for i in range(4)]
# # 上，右，下，左四个方向
# dir_x = [-1, 0, 1, 0]
# dir_y = [0, 1, 0, -1]
#
#
# # 深度搜索
# def dfs(x, y, now_number):
#     global ans
#     """
#     :param x: 当前所在的行
#     :param y: 当前所在的列
#     :param now_number: 当前填充的数字
#     :return:
#     """
#     # 搜索边界，填完了16个数字就可以
#     # 没有进一步的要求
#     if now_number == 16:
#         ans += 1
#         return
#     # 搜索
#     # 向四个方向
#     for i in range(4):
#         new_x = x + dir_x[i]
#         new_y = y + dir_y[i]
#         # 如果没有越界，且当前位置没有填充数字
#         if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (not visit[new_x][new_y]):
#             # 标记
#             visit[new_x][new_y] = True
#             # 进行搜索,填下一个数字
#             dfs(new_x, new_y, now_number + 1)
#             # 回退，取消标记
#             visit[new_x][new_y] = False
#
#
# # 对格子的每一个位置进行试探
# for i in range(4):
#     for j in range(4):
#         visit[i][j] = True
#         dfs(i, j, 1)
#         visit[i][j] = False
#
# print(ans)


#大题
#F oi
# tian_gan = ['jia', 'yi', 'bing', 'ding', 'wu', 'ji', 'geng', 'xin', 'ren', 'gui']
# di_zhi = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']
#
# tianganyuan = ['geng', 'xin', 'ren', 'gui','jia', 'yi', 'bing', 'ding', 'wu', 'ji']
# dizhiyuan = ['shen', 'you', 'xu', 'hai','zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei']
# n = int(input())
# ans = ''
# ## 公园元年 0 年 geng shen庚申年
# k1 = n % 10
# k2 = n % 12
# n_tiangan = tianganyuan[k1]
# n_dizhi = dizhiyuan[k2]
# ans = n_tiangan+n_dizhi
# print(ans)

#G  思维
# def main():
#     k1 = int(input())
#     s = input().strip()
#     n = len(s)
#     k = n // k1
#     ans = 0
#     if k == 1:
#         for i in s:
#             if i != s[0]:
#                 ans += 1
#         print(ans)
#         return
#     r = []
#     if n % k != 0:
#         print(-1)
#         return
#     for i in range(0, n, k):
#         d = ""
#         for j in range(i, i + k):
#             d += s[j]
#         r.append(d)
#     maxV = 0
#     n1 = len(r)
#     for i in range(n1):
#         if maxV < r.count(r[i]):
#             maxV = r.count(r[i])
#     sm = ""
#     for i in range(n1):
#         if r.count(r[i]) == maxV:
#             sm = r[i]
#             break
#
#     for i in range(0, n, k):
#         ind = 0
#         for j in range(i, i + k):
#             if sm[ind] != s[j]:
#                 ans += 1
#             ind += 1
#     print(ans)
#
#
# main()

#H 读题/排序
# n = int(input().strip())
# nums = [list(map(int,input().split())) for _ in range(n)]
# r = []
# for i in range(n):
#     r.append([sum(nums[i]),nums[i][2]])
# r.sort()  #key=lambda x: x[1]
# ans = 0
# s = 0
# for i in range(n):
#     ans += r[i][0]-r[i][1] + s
#     s += r[i][0]
# print(ans)

#i  bfs Dijkstra


#J  DP + 递推
import time
start1 = time.perf_counter()

# 输入 k p l，空格分隔
k, p, L = map(int, input("input k p L separated by one spaces:").split())
# 1、生成二维数组，0层存 第一步小于p的方案数，1层存 总方案数
# 最小数组长度
len = k + 1
dp = [[0 for e1 in range(2)] for e in range(len)]
# 赋值 L=0 的情况
dp[0][0] = 1
dp[0][1] = 1
i = 0  # 定义循环写入的角标
# L为总距离数
for l in range(1, L + 1):  # l无用
    # 循环改变数组列角标，取模
    i = (i + 1) % len
    # 临时值，用于将 第一步小于p的方案数 与
    # 第一步大于等于p的方案数相加
    sum = 0
    # 2、开始计算 第一步小于p的方案数，存储在二维数组的0层
    for j in range(1, p):
        sum += (dp[(i - j) % len][1]) % 20201114
    dp[i][0] = sum  # 记录 第一步小于p的方案数
    # 3、开始计算 第一步大于等于p的方案数
    for o in range(p, k + 1):
        # 之前sum已经是 第一步小于p的方案数
        # 这里直接相加就等于总方案数啦
        sum += dp[(i - o) % len][0] % 20201114
    dp[i][1] = sum  # 4、记录总方案数，存储在二维数组的1层
# 5、循环结束，直接获取对应角标的1层即是 总方案数
print((dp[i][1]) % 20201114)



end2 = time.perf_counter()
print('Running time: %s Seconds' % (end2 - start1))







