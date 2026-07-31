"""
プログラム名：Kadai12-2.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""


class Chara:
    def __init__(self):
        self.name = "諸岡"     
        self.cm = 166.6        

    def syoukai(self):
        print(f"{self.name},身長 {self.cm}cm")

jinbutu = Chara()   
jinbutu.syoukai()   
