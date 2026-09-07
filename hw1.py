rice=45
sugar=40
oil=130
cus_rice=3
cus_sugar=2.5
cus_oil=1.8
rice_total=(rice*cus_rice)
sugar_total=(sugar*cus_sugar)
oil_total=(oil*cus_oil)
print("Rice Total",rice_total)
print("Sugar Total",sugar_total)
print("Oil total"+oil_total)
totalbill=rice_total+sugar_total+oil_total
print(totalbill)
total_int=int(totalbill)
print(total_int)
total_str=str(totalbill)
print(total_str)
import random
deliverycharge=random.randrange(5,10)
final=deliverycharge+totalbill
print(final)
