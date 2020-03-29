premium = 125.00

def ground_shipping(weight):
  cost = 0
  if (weight < 2):
    cost = (weight * 1.50) + 20
  elif (weight > 2) and (weight <=6):
    cost = (weight * 3.00) + 20
  elif (weight) > 6 and (weight <= 10):
    cost = (weight * 4) + 20
  else:
    cost = (weight * 4.75) + 20
  return cost

def drone_shipping(weight):
  cost = 0
  if (weight <=2):
    cost = (weight * 4.50) + 0.00
  elif (weight > 2) and (weight <=6):
    cost = (weight * 9.00) + 0.00
  elif (weight) > 6 and (weight <= 10):
    cost = (weight * 12.00) + 0.00
  else:
    cost = (weight * 14.25) + 0.00
  return cost

def cheapest(weight):
  ground = ground_shipping(weight)
  drone= drone_shipping(weight)
  if (ground < drone) and (ground < premium):
    print('The cheapest method is ground and it cost {} '.format(ground))
  elif (drone < ground) and (drone < premium):
     print('The cheapest method is drone and it cost {} '.format(drone))
  else:
    print('The chepeast method is premuim and it cost {} '.format(premium))
          
      
      
    

print(ground_shipping(40))
print(drone_shipping(40))
cheapest(40)


    
 
