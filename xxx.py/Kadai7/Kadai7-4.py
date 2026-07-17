"""
プログラム名：Kadai7-4.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
tosi = int(input('年齢入力>>'))
if tosi >= 10:
    print('このアトラクションは利用可能です。')
else:
    tukisoi = int(input('付き添い(有:1、無:0)>>'))

    if tosi < 10 and tukisoi == 1:
        print('このアトラクションは利用可能です。')
    else:
        print('このアトラクションは利用できません。')