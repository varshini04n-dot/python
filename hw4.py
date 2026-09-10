webDevlopement=['Varshini','Kows','Bismi']
DataScience=['Arthi','Raji','Sanj']
uiux=['prathisma','isma','chandra']
all_participants=[webDevlopement,DataScience,uiux]
webDevlopement.append('sanji')
print(webDevlopement)
DataScience.insert(1,'nithi')
print(DataScience)
uiux.pop()
print(uiux)
copy_datascience=DataScience.copy()
del DataScience
print(webDevlopement[:2])
print([len(x) for x in copy_datascience])
print("Asha" in all_participants)
tup=(webDevlopement[0],copy_datascience[0],uiux[0])
print(tup)