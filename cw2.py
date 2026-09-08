
book="""BOOK RECEIPT 
-----------------------"""
book1="Python Basics"
price1=450
book2="Data Science Intro"
price2=600
line1=("Book Title :{}-{}".format(book1,price1))
line2=("Book Title :{}-{}".format(book2,price2))
total=price1+price2
line3=("T0tal Price{}".format(total))
thankyou="Thank-You"
final=(line1+"\n"+line2+"\n"+line3+"\n"+"\t"+thankyou)
print(final.upper())