"""
プログラム名：Ren10-4.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
print('加算プログラム Ver.2')
opt1 = int(input('1 つめのオペランド>>'))
opt2 = int(input('2 つめのオペランド>>'))
def kasan_ver2(w_opt1,w_opt2):
    total = w_opt1 + w_opt2
    print(f'{w_opt1}+{w_opt2}={total}')
kasan_ver2(opt1,opt2)