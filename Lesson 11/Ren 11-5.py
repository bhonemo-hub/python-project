"""
プログラム名：Ren11-5.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def in_ninzu(it):
    print(f'{it}情報処理科の各人数を入力します')
    zaiseki = int(input('在籍数>>'))
    goukaku = int(input('基本情報試験合格者数>>'))
    ninzu = [zaiseki,goukaku]
    return ninzu

def wariai_keisan(ninzu):
    ritu = ninzu[1]/ninzu[0] * 100
    return ritu

def out_ritu(it,ritu):
    print(f'{it}情報処理科の{ritu}取得率は')

cd_ninzu = in_ninzu('情報処理科')
is_ninzu = in_ninzu('ITスペシャルリス科')
cd_ritu = wariai_keisan(cd_ninzu)
is_ritu = wariai_keisan(is_ninzu)
out_ritu('情報処理科',cd_ritu)
out_ritu('ITスペシャルリスト科',is_ritu)