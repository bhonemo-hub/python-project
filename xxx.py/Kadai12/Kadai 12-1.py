"""
プログラム名：Kadai12-1.py
作成日：2026年07月24日
作成者：CD71-3組 K026C2043 ミャットボーンカイン
"""

class watasi:
    def __init__(self):
        self.name = "諸岡"   
        self.money = 200     

    def cyokin(self, add: int):
        print(f"{self.name}は{add}万円儲かった！")
        self.money += add


print("私の秘密を紹介します")

wk = watasi()      
wk.cyokin(1000)    
print(f"{wk.name}の貯金は現在{wk.money}万円です")
