"""
プログラム名：Ren11-4.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def heikin_ver2(w_data):
    avg = sum(w_data)/len(w_data)
    

print('クラス平均表示プログラム Ver.2')
data = list()
for num in range(4):
    ten = int(input(f'{num+1}組の点数>>'))
    data.append(ten)
kekka = heikin_ver2(data)
print(f'4クラス平均：{kekka}点')
