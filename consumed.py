x=float(input("Enter unit  charge : "))
if(x<=50) :
     amount = 0.50*x
     print("Amount : ",amount)
elif(x<=150):
     amount=25+((x-50)*0.75)
     print("Amount : ",amount)
elif(x<=250):
     amount=100+((x-150)*1.20)
     print("Amount : ",amount)
elif(x>250):
     amount=220+((x-250)*1.50)
     print("Amount : ",amount)