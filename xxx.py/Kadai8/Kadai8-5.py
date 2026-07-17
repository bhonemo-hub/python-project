"""
プログラム名：Kadai8-5.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
data = [22, 34, 56, 33, 42, 83, 27, 18, 25, 89]
min_value = data[0]
min_index = 0
i = 0 
while i < len(data):
    if data[i] < min_value:
        min_value = data[i]
        min_index = i
    i += 1
print(data)
print(f'data[{min_index}]が最小で最小値は{min_value}です')