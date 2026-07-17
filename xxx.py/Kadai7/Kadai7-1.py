"""
プログラム名：Kadai7-1.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
a = int(input('1つ目の値入力>>'))
b = int(input('2つ目の値入力>>'))
if a > b:
    big = a
    small = b
else:
    big = b
    small = a

ans = big - small
print(f'大きい方から小さい方を引くと {big}-{small} で答えは {ans} です.')