"""
プログラム名：Code4-4.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
is_wake = True
count = 0
while is_wake == True:
    count += 1
    print(f'ひつじが{count}匹')
    key = input('もう眠りそうですか？(y/n)>>')
    if key == 'y':
        is_wake = False
print('おやすみなさい')