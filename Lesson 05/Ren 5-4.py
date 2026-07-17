"""
プログラム名：Ren5-4.py
作成日：2026年5月29日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
tatemono = ['地下1階','1階','2階','3階','4階']
print('現在の建物のフロア状況')
print(tatemono)

tatemono.append('屋上')
print('\n屋上が完成しました')
print(tatemono)

tatemono.remove('地下1階')
print('\n地下 1 階を閉鎖しました')

tatemono[3] = 'M2階'
print('\n3階を M2 階に改装しました')
print(tatemono)
