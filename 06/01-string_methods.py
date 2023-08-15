text = "Positive anything is better than negative nothing."
    
text1 = "POSitivE ANYtHING iS BETTER THaN NEGETIVE NoTHING"
#       "posITIVe anyThing Is better thAn negetive nOthing"

# methods  --> revesh

#******************************
# print(text.capitalize())  # capitalize  avalin harf az avvalin kelemeh jomleh bozorg mikone
#****************casefold , lower , upper , swapcase***************

# print(text1.casefold())
# print(text1.lower()) # casefold = lower --> feghat tabdil hooroof bozorg be koochak
# print(text.upper())  # feghat tabdil temam hooroof koochak be bozorg
# print(text1.swapcase())  # ham kar upper ham kar lower  be in soorat ke agar koochak bood tabdil be bozorg va agar ham bozorg bood tabdil be koochak

#**************center**********************
# print("python".center(31 ,"@")) # be markaz bordan "python"

# **************endswith , startswith*****************
# print(text.endswith("nothing."))  # agar jomleh ba argoman dakhel perantexz temam shevad TRue bar migardand
# print(text.startswith("positive")) # agar jomleh ba argoman dekhel perantez shoroo shevad True baermigardanad
# 
#*************count***************
# # count(substr,start, end) --> zirreshteh 
# print(text.count("p"))
# print(text.count("t"))
# print(text.count("t",2,7))  # count miad misheomarad harche ke be onvan argoman dakhel perantezash
# print(text.count("som"))

#******************index find**************************
# yaftan chizi(arguman ya harche dakhel perantez bood dar text
# find , index shomarh avalin khane jaye ke chiz ma shoroo mishe 
# text2 = "python"
# print(text2.find("yth"))
# print(text2.index("yth"))
# print(text.index("som",start ,end)) # az koja ta koja 
# print(text.find("som",start ,end)) # az koja ta koja 
# # tefovoot --> 
# print(text2.find("som"))  # agar chizi ke dakhel perantez hast payda neshod -1 barmigardand 
# print(text2.index("som"))  # agar chizi ke dakhel perantez hast payd neshod error not found barmigardand
# 
#***********************title*****************************************
# avval temam keleat dar jomleh bozorg shevad --> text.title()
# print(text.title())

# tevajoh ************harchizi.join(string)*****************
# text4 = "som soltani is student in nohoom class"
# print("Som*".join(text4))  # pas "HARCHIZI".joint(string)  miad harja ke harfi bood badash heman HARCHIZI mizare

#****************strip*************
# text3 = "**python*"
# print(text3.strip("*pon"))  # avval va ahkar hazf mikonad  on chizi ke dakhel perantez hast 
# print(text3.rstrip("*")) # rightsrip  # an chizi ke dakhek perantez hast az samt rast hazf mikonad 
# print(text3.lstrip("*")) # leftstrip  harchizi dahkel perantez bood az chap feghat hazf mikonad

# ****************split**********************
# text.split("str") --> bar asas str miad list dorost mikonad yani dakhel in  [] har ja str bood bia bejash , bezar
# 
# text4 = """s o m s o l t a n i
# javij
# qoli"""
# print(text4.split(" "))
# print(text4.splitlines())  # shakht list bar asas line ha 
# 
# ***************** replace(str1,str2,count)  ********
# count --> tedad jaigaozin ha ra moshakas mikonad
# text6 = "havij havij levashak" 
# print(text6.replace("havij","qoli" ,1)) # miasd arguman aval agar payda konad ba arguman dovvom jigozin mikonand
# print(text6.replace("fox","qoli" ))
#

#************ isalnum
print("59874985748793som".isalnum()) # agar hooroogf va adad bood True bargardan 

