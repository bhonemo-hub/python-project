"""
プログラム名：Kadai10-1.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
scores = [30,59,100,48,60]
ng_scores = list()
for ten in scores:
    if ten < 60:
        ng_scores.append(ten)
print(f'全員の得点:{scores}')
print(f'不合格者の得点:{ng_scores}')