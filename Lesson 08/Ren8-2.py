"""
プログラム名：Ren8-2.py
作成日：2026年6月26日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
tensuu = int(input('点数を入力してください>>'))
if tensuu > 100:
    print('点数は 0 以上 100 の範囲で入力してください')
elif tensuu > 90:
    print('評価は S です')
elif tensuu >= 80:
    print('評価は A です')
elif tensuu >= 70:
    print('評価は B です')
elif tensuu >= 60 :
    print('評価は C です')
elif tensuu >= 0 :
    print('評価は D です')
else:
    print('点数は 0 以上 100 の範囲で入力してください')