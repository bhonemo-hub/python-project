"""
プログラム名：Kadai7-2.py
作成日：2026年6月19日
作成者:CD71-3組K026C2043ミャットボーンカイン
"""
height_cm = float(input('身長(cm)>>'))
weight = float(input('体重(kg)>>'))

height_m = height_cm / 100

bmi = weight / height_m / height_m
bmi_int = int(bmi)

print('BMI=' + str(bmi_int))

if bmi_int >= 25:
    print('肥満')
else:
    print('正常')