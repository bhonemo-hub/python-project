"""
プログラム名：Kadai11-1.py
作成日：2026年07月17日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
def plus(x, y):
    # x と y の加算結果を返す
    answer = x + y
    return answer

def minus(x, y):
    # x と y の減算結果を返す
    answer = x - y
    return answer

# メイン処理
print("加算は 1、減算は 2 を入力してください>>", end="")
mode = int(input())

print("1 つめのオペランド>>", end="")
a = int(input())

print("2 つめのオペランド>>", end="")
b = int(input())

# 加算か減算かで分岐
if mode == 1:
    result = plus(a, b)
    print("足し算の答えは", result, "です")
elif mode == 2:
    result = minus(a, b)
    print("引き算の答えは", result, "です")
else:
    print("1 または 2 を入力してください")