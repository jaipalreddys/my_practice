weight = 8.4 
#Ground Shipping
ground_shiping =0
if weight <= 2:
  ground_shiping = weight*1.5 + 20
elif weight >=2 and weight <=6:
 ground_shiping =  weight*3 + 20
elif weight >=6 and weight<=10:
 ground_shiping = weight*4 +20
elif weight > 10:
 ground_shiping = weight*4.75 + 20

print("Ground Shipping : " + str(ground_shiping))

ground_shipping_pr = 125
print("Ground Shipping Premium:" + str(ground_shipping_pr))

#Drone Shipping
drone_shipping = 0
if weight <= 2:
  drone_shipping = weight*4.50
elif weight >=2 and weight <=6:
  pdrone_shipping = weight*9
elif weight >=6 and weight<=10:
  drone_shipping = weight*12
elif weight > 10:
  drone_shipping = weight*14.25

print("Drone Shipping: "+ str(drone_shipping))

#Cheapest Shipping
if ground_shiping < ground_shipping_pr and ground_shiping < drone_shipping:
  print("Ground Shipping is the Cheapest")
elif ground_shipping_pr < ground_shiping and ground_shipping_pr < drone_shipping:
    print("Ground Shipping Premium is the Cheapest")
else:
    print("Drone Shipping is the Cheapest")