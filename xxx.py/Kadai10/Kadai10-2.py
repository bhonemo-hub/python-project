"""
プログラム名：Kadai10-2.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
print('3 値の掛け算プログラム')
opt1 = int(input('1 つめの値>>'))
opt2 = int(input('2 つめの値>>'))
opt3 = int(input('3 つめの値>>'))

def kakezan(w_opt1,w_opt2,w_opt3):
    total = w_opt1 * w_opt2 * w_opt3
    print(f'{w_opt1}x{w_opt2}x{w_opt3}={total}')

kakezan(opt1,opt2,opt3)