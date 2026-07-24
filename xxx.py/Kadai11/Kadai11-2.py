"""
プログラム名：Kadai11-2.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def max_syori(num1, num2):
    # num1 と num2 の大きい方を返す
    if num1 > num2:
        return num1
    else:
        return num2

def min_syori(num1, num2):
    # num1 と num2 の小さい方を返す
    if num1 < num2:
        return num1
    else:
        return num2

def kagen_syori(num1, num2):
    # num1 が大きい → 和
    # num2 が大きい → 差（num2 - num1）
    if num1 > num2:
        ans = num1 + num2
    else:
        ans = num2 - num1
    return ans

# メイン処理
print("1 つめの値>>", end="")
num1 = int(input())

print("2 つめの値>>", end="")
num2 = int(input())

# 大きい方
big = max_syori(num1, num2)
print(num1, "と", num2, "では", big, "が大きいです")

# 小さい方
small = min_syori(num1, num2)
print(num1, "と", num2, "では", small, "が小さいです")

print("1 番目が大きい時は和、2 番目が大きい時は差を求めます")

# 和または差
ans = kagen_syori(num1, num2)
print("値は", ans, "です")