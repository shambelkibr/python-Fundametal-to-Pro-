incame= float(input("enter the salarry get work"))
if incame> 601 and incame<1500:
    tax =(incame*10)/100
elif incame >1501 and incame <4000:
    tax=(incame*15)/100
elif incame >4001 and incame <10000:
    tax=(incame*20)/100
elif incame >10001 and incame <20000:

    tax=(incame*25)/100
else:
    tax=(incame*30)/100