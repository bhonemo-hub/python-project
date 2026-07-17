"""
プログラム名：Ren8-1.py
作成日：2026年6月26日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
a = int(input('整数を入力>>'))
amari = a % 2

if a >= 0 and amari %2== 0:
    print('偶数')
else:
    print('奇数か、または0以上ではありません')
