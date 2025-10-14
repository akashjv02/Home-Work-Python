Rice = 45
Sugar = 40
Oil = 130

rice_q = 3
sugar_q = 2.5
oil_q = 1.8

total_rice = Rice * rice_q
total_sugar = Sugar * sugar_q
total_oil = Oil * oil_q

total_bill = total_rice + total_sugar + total_oil

print("Total rice = ", total_rice)
print("Total sugar = ", total_sugar)
print("Total oil = ", total_oil)
print("Total bill = ", total_bill)

print("Final bill as a integer = ", int(total_bill))
print("Final bill as an string = ", str(total_bill))

print("Convert the float value = ", float(total_bill))

import random
delivery_charge = random.randrange(5,10)

print("Delivery charge = ",delivery_charge)

final_billwdel = total_bill  + delivery_charge
print("Final bill with delivery charge = ", final_billwdel)



