"""
プログラム名：Kadai7-3.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""

ten = []


for i in range(3):
    score = int(input(f"{i+1} 人目の点数:"))
    ten.append(score)


total = sum(ten)
avg = total / len(ten)


print(f"合計は {total} 点です")
print(f"平均は {avg} 点です")


for i in range(3):
    if ten[i] >= avg:
        print(f"{i+1} 人目の点数は {ten[i]} 点、平均点以上です。")
    else:
        print(f'{i+1} 人目の点数は {ten[i]} 点、平均点未満です。')