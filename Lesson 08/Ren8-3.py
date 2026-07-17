"""
プログラム名：Ren8-3.py
作成日：2026年6月26日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
atai1 = str('10')
atai2 = str('20')
print(f'1 つめの値={atai1}、2 つめの値={atai2}')
flg = input('入力区分(引き算:1/文字連結:2)>>')
if flg == '1':
    num1 = int(atai1)
    num2 = int(atai2)
    if num1 > num2:
        print(f'大きい値から小さい値を引き算した結果は {num1 - num2} です')
    else:
        print(f'大きい値から小さい値を引き算した結果は {num2 - num1}です')
else:
    print(f'文字を連結すると{atai1+atai2}です')
