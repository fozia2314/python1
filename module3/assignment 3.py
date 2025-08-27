gender =input("Enter biological gender (male/female):").lower()
hemoglobin =float(input(" Enter hemoglobin value (g/l): "))
if gender =="female":
    if hemoglobin <117 :
       print("Your hemoglobin is low.")
    elif hemoglobin <=155 and hemoglobin >=117 :
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high. ")
if gender =="male":
   if hemoglobin <134 :
      print("Your hemoglobin is low.")
   elif hemoglobin <=167 and hemoglobin >=134 :
      print("Your hemoglobin is normal.")
   else:
      print("Your hemoglobin is high.")
if gender !="female" and gender !="male":
      print("Invalid gender.")