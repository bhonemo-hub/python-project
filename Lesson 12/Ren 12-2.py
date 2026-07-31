"""
プログラム名：Ren12-2.py
作成日：2026年07月24日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
IT = 'IT スペシャルリスト科'
def it_print():
    global IT
    IT = '情報処理科'
print(f'変更前のグローバル変数 IT の内容:{IT}')
it_print()
print(f'変更後のグローバル変数 IT の内容:{IT}')
