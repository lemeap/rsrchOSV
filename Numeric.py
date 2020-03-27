# -*- coding: utf-8 -*-
import numpy as np
import math
from scipy.optimize import fsolve

"""
fp = lambda mp: np.sqrt(g * np.asarray(mp) / cd)
func의 설정 예제
"""

def calIncSearch(func, xmin, xmax, ns):
    """
        증분법을 계산하는 함수입니다.
        param func: target function
        param xmin: minimum value of x
        param xmax: maximum value of x
        ns: unit step size
    """
    # set range of x
    x = np.linspace(xmin, xmax, ns)

    # function value of target function
    f = func(x)

    # step number of interval range
    nb = 0
    xb = []

    # 0부터 설정한 최고값까지 반복
    for k in np.arange(np.size(x) - 1):
        # 만약 f(x)랑 f(x+1)이 부호가 다르면 = 그래프가 x축을 뚫고 지나갔으면
        if np.sign(f[k]) != np.sign(f[k + 1]):
            # 구간 하나 찾음!
            nb = nb + 1

            # 여기부터 여기까지임
            xb.append(x[k])
            xb.append(x[k + 1])

    # 구간 갯수(Number of Brackets), 구간 배열(Root Interval) 반환
    return nb, xb

def calBisection(func, floXLower, douXUpper):
    """
        이분법을 계산하는 함수입니다.
        func : 대상 함수
        floXLower : 계산할 x의 최저값 (lower guesses)
        flowXUpper : 계산할 x의 최고값 (upper guesses)
        Bisection은, 계산할 x의 최저값과 최고값이 부호가 달라야 합니다.
        중간값 정의에 의해, 그 사이에 무조건적으로 근이 존재하기 때문입니다.
        그러나 f(최저값)과 f(최고값)을 곱한 값이 양수라면, 부호가 같다는 뜻이 됩니다.
        계산이 불가능하다는 뜻이므로, 함수를 종료합니다.
    """
    # 최대 반복 횟수, 기본 100으로 설정함
    intMaxIter = 100

    # 예상된 오차의 범위, 기본 0.0001%로 설정
    es = 1.0e-4

    # f(최저값)과 x(최고값)을 곱함
    test = func(floXLower) * func(douXUpper)
    if test > 0:
        print("No sign change")
        return [], [], [], []

    # 반복 카운터
    intIter = 0

    # 중심값 초기화
    xr = floXLower

    # 계산될 오차값 100%로 초기화
    ea = 100

    # 무한 반복
    while True:
        # 우선 현재 중심값을 floXRetunOld라는 변수에 저장해둠
        floXRetunOld = xr

        # 중심값을 현재의 최고, 최저값을 더한 후 2로 나눈 값(중앙값)으로 설정함
        xr = np.float((floXLower + douXUpper) / 2)

        # 한 바퀴 더 돌았음
        intIter = intIter + 1

        # 중심값이 0이 아니라면
        if xr != 0:
            # 다음 식을 계산해서 오차값을 찾음
            # or{(현재 중심값) - (이전 중심값)} / (현재 중심값) or * 100
            ea = np.float(np.abs((np.float(xr) - np.float(floXRetunOld)) / np.float(xr)) * 100)

        # f(최저값)과 x(최고값)을 곱함
        test = func(floXLower) * func(xr)

        # 만약 곱한 값이 양수라면
        if test > 0:
            # 최저값을 현재 중심값으로 설정함
            floXLower = xr
        # 아니고 만약 음수라면
        elif test < 0:
            # 최고값을 현재 중심값으로 설정함
            douXUpper = xr
        # 만약 양수도, 음수도 아닌 0이라면
        else:
            # 오차 없음, 정확히 찾음
            ea = 0

        # 만약 (1) 계산된 오차값이 허용된 오차값보다 작다면 = 대강 이쯤되면 답이다 싶으면
        # 또는
        # 만약 (2) 설정한 최대 반복값보다 더 많이 돌았으면
        if np.int(ea < es) or np.int(intIter >= intMaxIter):
            # 계산 그만, 반복 종료
            break

    # 구한 중심값을 근으로 침
    floRoot = xr

    # f(x)에 구한 근 넣어서 계산
    fx = func(xr)

    # 근, f(근) 값, 계산된 오차값, 반복값
    return floRoot, fx, ea, intIter

def calFalsePosition(func, floXLower, douXUpper):
    """
        가위치법을 계산하는 함수입니다.
        func : 대상 함수
        floXLower : 계산할 x의 최저값 (lower guesses)
        flowXUpper : 계산할 x의 최고값 (upper guesses)
    """
    # 최고 반복 한계값, 에러 최댓값 설정
    intMaxIter = 100
    es = 1.0e-4

    # f(최저값)과 x(최고값)을 곱함
    test = func(floXLower) * func(douXUpper)

    """
        False Position은 Bisection과 마찬가지로 구간을 기반으로 판단하는 알고리즘입니다.
        그러므로 역시 중간값 정리를 적용하여, 양쪽 끝값의 부호가 달라야 계산이 가능합니다.
        그렇지 않다면, 계산을 하지 않고 함수를 종료합니다.
    """
    if test > 0:
        print("No sign change")
        return [], [], [], []

    # 반복 카운터 초기화
    intIter = 0

    # 중간값 초기화
    xr = floXLower

    # 오차 초기화
    ea = 100

    # 무한 반복
    while True:
        # 이전 중간값 저장
        floXRetunOld = xr

        # False Position 알고리즘 : 삼각형의 닮은꼴 기반 계산법 (PPT 참조)
        xr = np.float(douXUpper - func(douXUpper) * (floXLower - douXUpper) / (func(floXLower) - func(douXUpper)))

        # 반복 카운터 1 증가
        intIter = intIter + 1

        # 중간값이 0이 아니면
        if xr != 0:
            # 다음 식을 계산해서 오차값을 찾음
            # or{(현재 중심값) - (이전 중심값)} / (현재 중심값) or * 100
            ea = np.float(np.abs((np.float(xr) - np.float(floXRetunOld)) / np.float(xr)) * 100)

        # f(최저값)과 x(최고값)을 곱함
        test = func(floXLower) * func(xr)

        # 만약 곱한 값이 양수라면
        if test > 0:
            # 최저값을 현재 중심값으로 설정함
            floXLower = xr
        # 아니고 만약 음수라면
        elif test < 0:
            # 최고값을 현재 중심값으로 설정함
            douXUpper = xr
        # 만약 양수도, 음수도 아닌 0이라면
        else:
            # 오차 없음, 정확히 찾음
            ea = 0

        # 만약 (1) 계산된 오차값이 허용된 오차값보다 작다면 = 대강 이쯤되면 답이다 싶으면
        # 또는
        # 만약 (2) 설정한 최대 반복값보다 더 많이 돌았으면
        if np.int(ea < es) or np.int(intIter >= intMaxIter):
            # 계산 그만, 반복 종료
            break

    # 찾은 중심값을 근으로 함
    floRoot = xr

    # f(근) 계산
    fx = func(xr)

    # 근, f(근), 오차, 반복 횟수 반환
    return floRoot, fx, ea, intIter

def calNewtonRaphson(func, dfunc, xr):
    """
        Newton-Raphson을 계산하는 함수입니다.
        func : 대상 함수
        dfunc : 대상 함수의 미분 함수
        xr : 시작값
    """
    # 최대 반복 횟수, 오차 최댓값, 반복 카운터 초기화
    intMaxIter = 50
    es = 1.0e-4
    intIter = 0

    # 무한 반복
    while True:
        # 현재 값 보관
        floXRetunOld = xr

        # Newton-Raphson Algorithm 계산
        xr = np.float(xr - func(xr) / dfunc(xr))
        # 반복 카운터 1 증가
        intIter = intIter + 1

        # xr이 0이 아닐 경우
        if xr != 0:
            # 다음 식을 계산해서 오차값을 찾음
            # or{(현재 중심값) - (이전 중심값)} / (현재 중심값) or * 100
            ea = np.float(np.abs((np.float(xr) - np.float(floXRetunOld)) / np.float(xr)) * 100)

        # 만약 (1) 계산된 오차값이 허용된 오차값보다 작다면 = 대강 이쯤되면 답이다 싶으면
        # 또는
        # 만약 (2) 설정한 최대 반복값보다 더 많이 돌았으면
        if np.int(ea < es) or np.int(intIter >= intMaxIter):
            break

    # 구해진 xr을 근으로 함
    floRoot = xr
    # 근, 오차값, 반복 횟수 반환
    return floRoot, ea, intIter

def calSecant(func, x0, x1):
    """
        Secant Method(할선법)를 계산하는 함수입니다.
        func : 대상 함수
        x0, x1 : 시작값, 끝값
    """
    # 최대 반복 횟수, 최대 오차, 반복 카운터 초기화
    intMaxIter = 100
    es = 1.0e-4
    intIter = 0

    # 무한 반복
    while True:
        # Secant Method
        xr = np.float(x1 - (func(x1) * (x1 - x0) * 1.0) / (func(x1) - func(x0)))
        # 반복 카운터 초기화
        intIter = intIter + 1

        # xr이 0이 아닐 경우
        if xr != 0:
            # 다음 식을 계산해서 오차값을 찾음
            # or{(현재 구한 값) - (바로 전에 구한 값)} / (현재 구한 값) or * 100
            ea = np.float(np.abs((np.float(xr) - np.float(x1)) / np.float(xr)) * 100)

        # 만약 (1) 계산된 오차값이 허용된 오차값보다 작다면 = 대강 이쯤되면 답이다 싶으면
        # 또는
        # 만약 (2) 설정한 최대 반복값보다 더 많이 돌았으면
        if np.int(ea < es) or np.int(intIter >= intMaxIter):
            break

        # 값을 하나씩 뒤로 옮김
        x0 = x1
        x1 = xr

    # 구해진 xr을 근으로 함
    floRoot = xr
    # 근, 오차값, 반복 횟수를 반환
    return floRoot, ea, intIter

def calRKOde45(func, yinit, x_range, h):
    n = int((x_range[-1] - x_range[0])/h)

    x, y = x_range[0], yinit

    del x_range

    # Containers for solutions
    xsol, ysol = [x,], [y,]

    i = 0
    while i < n:
        k1 = func(x, y)

        yp2 = y + k1 * h / 2

        k2 = func(x+h/2, yp2)

        yp3 = y + k2 * h / 2

        k3 = func(x+h/2, yp3)

        yp4 = y + k3 * h

        k4 = func(x+h, yp4)

        y = y + (((k1 + k4) + (2 * (k2 + k3))) / 6 * h)
        del k1, k2, k3, k4, yp2, yp3, yp4
        x = x + h
        xsol.append(x)
        ysol.append([])
        i = i + 1
        ysol[i] = y
    ysol = np.array(ysol)
    return xsol, ysol