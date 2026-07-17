"""
プログラム名：Kadai5-2.py
作成日：2026年5月29日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
ten = []
score1 = int(input("1 人目の点数:"))
ten.append(score1)

score2 = int(input("2 人目の点数:"))
ten.append(score2)

score3 = int(input("3 人目の点数:"))
ten.append(score3)

# 合計と平均
total = sum(ten)
avg = total / len(ten)

print(f"合計は {total} 点です")
print(f"平均は {avg} 点です")

# 各人の点数と平均との差
print(f"1 人目の点数は {ten[0]} 点、平均との差 {ten[0] - avg} 点")
print(f"2 人目の点数は {ten[1]} 点、平均との差 {ten[1] - avg} 点")
print(f"3 人目の点数は {ten[2]} 点、平均との差 {ten[2] - avg} 点")