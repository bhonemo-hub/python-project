"""
プログラム名：Ren10-1.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
is_rpt = True
total = 0
while is_rpt == True:
    data = int(input('加算する数値を入力>>'))
    total += data
    key = input('計算を継続しますか?継続:y/終了:n>>')
    if key == 'n':
        is_rpt = False
print(f'合計は{total}です。')