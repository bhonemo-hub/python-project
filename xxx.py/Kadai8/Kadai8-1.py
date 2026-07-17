"""
プログラム名：Kadai8-1.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
flag = int(input('計算しますか?(する:1/しない:0)'))
if flag == 1:
    opt1 = int(input('1つめのオペランド>>'))
    ope = input('演算子>>')
    opt2 = int(input('2つめのオペランド>>'))
    if ope == '+':
        ans = opt1 + opt2
        print('答えは',ans)
    elif ope == '-':
        ans = opt1 - opt2
        print('答えは',ans)
    elif ope == '*':
        ans = opt1 * opt2
        print('答えは',ans)
    elif ope == '/':
        ans = opt1 % opt2
        print('答えは',ans)
    else:
        print('計算できません')
else:
    print('計算希望なしなので終了します')
    
