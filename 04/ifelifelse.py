# if , elif , else

# version 1 code 
dema = int(input("insert dema beraye bar avval"))
if dema > 30 :
    print("baba hava khaili atishe!")
if dema > 20 :
    print("baba heva toop toopoe")
if dema > 10 :
    print("hava havaye shomale")
else:
    print("baba hava yakh yakh hast")

#  version 2 code 
dema = int(input("insert dema beraye bar dovvom"))
if dema > 30 :
    print("baba hava khaili atishe!")
else:
    if dema > 20 :
        print("baba heva toop toopoe")
    else:
        if dema > 10 :
            print("hava havaye shomale")
        else:
            print("baba hava yakh yakh hast")

# version final
dema = int(input("insert dema beraye bar sevvom"))
if dema > 30 :
    print("baba hava khaili atishe!")
elif dema > 20 :
    print("baba heva toop toopoe")
elif dema > 10 :
    print("hava havaye shomale")
else:
    print("baba hava yakh yakh hast")
