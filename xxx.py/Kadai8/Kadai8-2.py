"""
プログラム名：Kadai8-2.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
atai1 = input('1 つめの値>>')
atai2 = input('2 つめの値>>')
flg = int(input('入力データ区分(数値:1/文字:2)>>'))
if flg ==  1:
    print('入力値が数値のため大小比較します')
    n1 = int(atai1)
    n2 = int(atai2)

    if n1 == n2:
        print('2 つの値は同じです')
    elif n1 > n2:
        print('1つめの値の方が大きいです')
    else:
        print('2 つめの値の方が大きいです')
elif flg == 2:
    print('入力値が文字のため文字連結します')
    print(atai1 + atai2)
else:
    print('区分が不正です')