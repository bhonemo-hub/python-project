"""
プログラム名：Code 6-5.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
class Hero:
    name = '松田'
    hp = 100
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝ました!')
        self.hp += hours
#ゲーム開始
print('スッキリファンタジーⅫ ~金色の理想郷~')
h = Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です。')