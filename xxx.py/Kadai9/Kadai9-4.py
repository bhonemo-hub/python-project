"""
プログラム名：Kadai9-4.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
data = [73, 59, 92, 83, 75, 52, 95, 70, 69, 80]

gusu = []  
kisu = []  

print(data)

i = 0
while i < len(data):
    if i % 2 == 0:
        gusu.append(data[i])
    else:
        kisu.append(data[i])
    i += 1

print(gusu)
print(kisu)