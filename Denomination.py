def no_notes(f):
  Q = [1000,500,200,100,50,20,10]
  e = 0
  for i in range(8):
   d1 = Q[i]
   e = f // d1
   print ("Notes of {} = {}".format(d1,e))
amount = int(input("Enter Total Amount"))
no_notes(amount)
          
