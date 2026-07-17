"""
プログラム名：Kadai11-3.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def kaijo(n):
    ans = 1
    while n > 0:
        ans *= n
        n -= 1
    return ans

# メイン処理
n = int(input("求めたい階乗 n を入力>>"))

if n < 0:
    print("{} の階乗は求められません。0 以上を入力してください。".format(n))
else:
    ans = kaijo(n)
    print("n={} のとき、n!={}".format(n, ans))