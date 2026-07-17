"""
プログラム名：Kadai9-3.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
data = [22, 34, 56, 33, 42, 83, 27, 18, 25, 89]

print(data)

start = int(input("どこから>>"))
end = int(input("どこまで>>"))

total = 0
i = start

while i <= end:
    total += data[i]
    i += 1

print(f"{start} 番めから {end} 番めまでの合計は {total} です")