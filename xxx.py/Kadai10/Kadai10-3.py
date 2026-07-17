"""
プログラム名：Kadai10-3.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
print('1 行あたり 7 個づつ表示します')
num = int(input('*をいくつ表示しますか>>'))
def out_syori(num):
    count = 0
    for i in range(num):
        print('*',end='')
        count += 1
        if count % 7 == 0:
            print('')
    if count % 7 == 0:
        print('')
out_syori(num)