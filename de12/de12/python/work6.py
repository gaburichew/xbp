print("閉校時間になっても寝てて閉じ込められてしまった!同じような仲間がいた!")
name=input("あなたの名前は？")
print("脱出しないと!どうしようか、周りを見渡す。同様先生のパソコンを見つけた!パスワードがある!これを開くと扉が開くらしいぞ!")
   
selecta=int(input("制限かかる前にどれを選ぶ？"))
if selecta==1:
    print("出れた!")
elif selecta==3:
    print("")
elif selecta==2:
    print("doyo.1000")
    print("出れた!")

    
print("扉が開いた!外に出よう!あれ？1階で火事が起きてる!出口は1階なのに!")
selectb=int(input("どうする？"))
if selectb ==1:
    print("下に行く")
    print("火事に巻き込まれて死")
elif selectb==2:
    print("火事に巻き込まれないように上へ行く")
    print("とりあえず火事から逃れることには成功した。")