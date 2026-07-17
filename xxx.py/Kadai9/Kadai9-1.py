"""
プログラム名：Kadai9-1.py
作成日：2026年07月03日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
test = int(input('いくつの段を練習しますか?1~9 を入力>>'))
for i in range (1,10):
    ans = int(input(f'{test}*{i}は？'))
    correct = test * i

    if ans == correct :
        print('正解です。')
    else :
        print(f'不正解です. 答えは{correct}でした.')

