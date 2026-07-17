"""
プログラム名：Ren9-2.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
scores = [80, 95, 98, 100]
total = sum(scores)
avg = total / len(scores)
print(scores)
print(f'平均点は{avg}点です。')
i = 1
for data in scores :
    if data >= avg:
        print(f'{i}組の得点は{data}点で平均点以上です。')
    else : 
        print(f'{i}組の得点は{data}点で平均点未満です。')
    i += 1