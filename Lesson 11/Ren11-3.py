"""
プログラム名：Ren11-3.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def heikin(w_data):
    avg = sum(w_data)/len(w_data)
    print(f'4 クラスの平均点:{avg}点')

data = list()
for num in range(4):
    ten = int(input(f'{num+1}組の点数>>'))
    data.append(ten)
heikin(data)