"""
プログラム名：Ren6-5.py
作成日：2026年6月12日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
uriage = {'kamata':65,'omori':110,'oimachi':50}
print('最初のディクショナリの内容:{}'.format(uriage))

uriage['kawasaki'] = 125
uriage['kamata'] = 70
del uriage['oimachi']

print('現在のディクショナリの内容:{}'.format(uriage))
total = sum(uriage.values())
print('3店舗合計:{}個'.format(total))