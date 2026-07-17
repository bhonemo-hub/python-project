"""
プログラム名：Kadai8-4.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
data = [22, 34, 56, 33, 42, 83, 27, 18, 25, 89]
max_value = data[0]
i = 0
while i < len(data):
    if data[i] > max_value:
        max_value = data[i]
    i += 1
print('最大値:',max_value)