"""
プログラム名：Kadai8-3.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
num = int(input('範囲を指定:'))

cnt = 1
sum_even = 0
while cnt <= num :
    if cnt % 2 == 0:
        sum_even += cnt
    cnt += 1

print(f'{num}までの偶数の和は {sum_even} です')
