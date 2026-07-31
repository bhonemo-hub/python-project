"""
プログラム名：Ren12-3.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
class HERO:
    name = 'モロロッケ' 
    hp = 100
    def sleep(self,hours):
        print('{} は {} 時間寝た!'.format(self.name,hours))
        self.hp += hours

#ゲーム開始
print('工学院ファンタジー')
h = HERO()
h.sleep(3)
print('{}のHPは現在{}です。'.format(h.name,h.hp))