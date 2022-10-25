name=input("名前を教えて下さい")
waist=input("腹囲は？")
age=input("年齢は？") 
if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")
if age>=40:
    print(name,"さん、40歳以上でwaist85以上はなかなかですね~")
elif age==40:
    print(name,"さん、40歳ならまだ間に合います。頑張ってダイエットしてください。")
else:
    print(name,"さん、まあギリですけど体調には気を使ってくださいね")