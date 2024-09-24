from typing import List


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(c) for c in input().split(" ")]

    vst = set()
    def check(nums: List[int]) :
        A, B, C, AB, AC, BC, ABC = nums
        cnt = 0
        for i in (A, B, C):
            if i: cnt += 1
  # 尝试推出 A,B,C。
        # 给了七个组合中任意4个，必然可以求出 A,B,C
        while cnt < 3:
            if not A:
                if ABC and BC:
                    A = ABC - BC
                    cnt += 1
                elif AB and B:
                    A = AB - B
                    cnt += 1
                elif AC and C:
                    A = AC - C
                    cnt += 1
            if not B:
                if ABC and AC:
                    B = ABC - AC
                    cnt += 1
                elif AB and A:
                    B = AB - A
                    cnt += 1
                elif BC and C:
                    B = BC - C
                    cnt += 1
            if not C:
                if ABC and AB:
                    C = ABC - AB
                    cnt += 1
                elif AC and A:
                    C = AC - A
                    cnt += 1
                elif BC and B:
                    C = BC - B
                    cnt += 1
        # 尝试推导矛盾
        if not (A <= B <= C) or (AB and A + B != AB) or (AC and A + C != AC) or (BC and B + C != BC) or (ABC and A + B + C != ABC):
            return False
        return (A,B,C)

    def dfs(index, i, cur):
        if i == N:
            global cnt
            #假设当前排列是 A B C AB AC BC ABC
            res = check(cur)
            if res:
                vst.add(res)
            #有可能排列的形式是 A B AB C AC BC ABC
            cur[2],cur[3] = cur[3], cur[2]
            res = check(cur)
            if res: vst.add(res)
            cur[2], cur[3] = cur[3], cur[2]
            return

        for j in range(index, 7):
            cur[j] = A[i]
            dfs(j+1, i+1, cur)
            cur[j] = 0
    dfs(0,0,[0,0,0,0,0,0,0])
    print(len(vst))