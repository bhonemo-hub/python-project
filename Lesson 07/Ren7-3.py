"""
プログラム名：Ren7-3.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
gakkaCd = 'CDISNT'
srch = input('探したい学科コードを入力>>')

if srch in gakkaCd: 
    print(f'文字列内に{srch}が見つかりました。')
else:
    print(f'文字列内に{srch}は見つかりません。')