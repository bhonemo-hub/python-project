"""
プログラム名：Kadai10-4.py
作成日：2026年07月10日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def sankaku(kigou, gyo):
    for i in range(gyo, 0, -1):
        print(kigou * i)

print("***花文字プログラム(逆三角形表示)***")
kigou = input("表示記号>>")
gyo = int(input("三角形の高さ>>"))

sankaku(kigou, gyo)