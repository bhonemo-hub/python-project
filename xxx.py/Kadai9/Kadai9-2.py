"""
プログラム名：Kadai9-2.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
scores = []

for i in range(1, 4):
    score = int(input(f"{i} 回目の得点入力>>"))
    scores.append(score)

for i in range(3):
    if i == 0:
        print(f"{i+1} 回目 {scores[i]} 点")
    else:
        diff = scores[i] - scores[i-1]
        if diff > 0:
            print(f"{i+1} 回目 {scores[i]} 点 +{diff} 点")
        else:
            print(f"{i+1} 回目 {scores[i]} 点 {diff} 点")
