"""
プログラム名：Code 6-3.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
userinfo = input('名前と血液型をカンマで図切って1行で入力>>')
[name,blood] = userinfo.split(',')
blood = blood.upper().strip()
print(f'{name}さんは{blood}型なので大古です。')