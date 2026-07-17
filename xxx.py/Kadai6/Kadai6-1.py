"""
プログラム名：Kadai6-1.py
作成日：2026年6月12日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
it = [88,90,95,100,99]
cd71 = it[:3]
is20 = it[3:]

cd71_total = sum(cd71[:])
cd71_avg = cd71_total/len(cd71[:])

is20_total = sum(is20[:])
is20_avg = is20_total/len(is20[:])

print(f"CD71 期、IS20 期の全ての点数={it}")
print(f"うち CD71 期の点数={cd71}")
print(f"うち IS20 期の点数={is20}")
print(f"CD71 期:合計{cd71_total}点、平均{cd71_avg}点")
print(f"IS20 期:合計{is20_total}点、平均{is20_avg}点")
