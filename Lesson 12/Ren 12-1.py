"""
プログラム名：Ren12-1.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def kake (x,y):
    answer = x * y
    return answer

def wari (x,y) :
    answer = x / y
    return answer

print('計算を行います')
key = input ('かけ算は a または A、わり算は b または B を入力>>')
ope1 = int(input('1 つめのオペランド>>'))
ope2 = int(input('2 つめのオペランド>>'))
if(key == 'a' or key == 'A'):
    kekka = kake (ope1,ope2)
    print(f'かけ算の答え:{kekka}')
else:
    kekka = wari(ope1,ope2)
    print(f'割り算の答え:{kekka}')