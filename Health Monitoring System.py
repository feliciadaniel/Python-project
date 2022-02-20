name=input("Enter name:")
age=int(input("enter age:"))
gender=input("If the patient is a male.Type'm'.If the patient is a female. Type'f':")
w=int(input("enter weight:"))
ht=float(input("enter height in metre:"))
bmi=w/(ht**2)
bpsys=int(input("Enter Systolic pressure:"))
bpdias=int(input("Enter diastolic pressure:"))
ldl=int(input("enter ldl cholestrol:"))
hdl=int(input("enter hdl cholestrol:"))
tri=int(input("enter triglyceride level:"))
glu=float(input("enter glucose levels for fasting glucose level test in mg/dL:"))
hemo=float(input("enter hemoglobin level in g/dL:"))
hema=float(input("enter hematocrit level in percentage:"))
plat=int(input("enter platelet count in mL :"))
wbc=int(input("Enter white blood cells count in mL:"))
print("RESULTS")
print()
print("Name:",name)
print("Age:",age)
if(gender=='m'):
    print("Gender: Male")
elif(gender=='f'):
     print("Gender: Female")
print("Weight:",w)
print("Height:",ht)
print()
print("BODY MASS INDEX")
print("Body Mass Index:",bmi)
if(bmi<18.5):
    print("Status : underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Status : normal")
elif(bmi>=25 and bmi<=29.9):
    print("Status : over weight")
else:
    print("Status : obese")
print()
print("BLOOD PRESSURE")
print("Blood Pressure:",bpsys,'/',bpdias)
if(bpsys<=90 and bpdias<=60):
    print("Status : hypotension")
elif(bpsys<120 and bpsys>90 and bpdias<80 and bpdias>60):
    print("Status : normal")
elif(bpsys>=120 and bpsys<=129 and bpdias<80):
    print("Status : elevated")
elif(bpsys>=130 and bpsys<=139 and bpdias>=80 and bpdias<=89):
    print("Status : stage 1 hyper tension")
elif(bpsys>=140 and bpdias>=90):
    print("Status : stage 2 hypertension")
else:
    print("your bp can't be categorised.Please check again")
print()
print("CHOLESTROL LEVELS")
print("LDL Cholestrol:",ldl,"mg/dL")
print("HDL Cholestrol:",hdl,"mg/dL")
if(ldl<100 and hdl>=60):
    print("Status : optimum")
elif(ldl>=100 and ldl<=129 and hdl>=50 and hdl<=59):
    print("Status : near optimum")
elif(ldl>=130 and ldl<=139 and hdl>=41 and hdl<=49):
    print("Status : increased risk")
elif(ldl>=160 and ldl<=189 and hdl>=35 and hdl<=40):
    print("Status : high risk")
elif(ldl>=190 and hdl<=35):
    print("Status : very high risk")
else:
    print("your ldl and hdl cholestrol level  can't be categorised.Please check again")
print("Triglyceride Cholestrol:",tri,"mg/dL")
if(tri<=100):
    print("Status : optimum")
elif(tri>=100 and tri<=149):
    print("Status : near optimum")
elif(tri>=150 and tri<=199):
    print("Status : increased risk")
elif(tri>=200 and tri<=399):
    print("Status : high risk")
elif(tri>=400):
    print("Status : very high risk")
else:
    print("your tri cholestrol level  can't be categorised.Please check again")
print()
print("BLOOD SUGAR LEVELS")
print("Glucose Levels:",glu,"mg/dL")
if(glu<100):
   print("Status : normal")
elif(glu>=100 and glu<=125):
    print("Status : prediabetes")
elif(glu>=126):
    print("Status : diabetes")
print()
print("COMPLETE BLOOD COUNT")
print("Hemoglobin:",hemo,"g/dL")
if(gender=='m'):
   if(hemo<13):
      print("Status : low")
   elif(hemo>=13 and hemo<=17):
       print("Status : normal")
   else:
       print("Status : high")
if(gender=='f'):
    if(hemo<11.5):
        print("Status : low")
    elif(hemo>=11.5 and hemo<=15.5):
        print("Status : normal")
    else:
        print("Status : high")
print("Hematocrit level:",hema,"%")
if(gender=='m'):
    if(hema<40):
        print("Status : low")
    elif(hema>=40 and hema<=55):
        print("Status : normal")
    else:
       print("Status : high")
if(gender=='f'):
    if(hema<36):
        print("Status : low")
    elif(hema>=36 and hema<=48):
        print("Status : normal")
    else:
        print("Status : high")
print("Platelet count:",plat,"/mL")
if(plat<150000):
   print("Status : low")
elif(plat>=150000 and plat<=400000):
    print("Status : normal")
else:
    print("Status : high")
print("WBC Count:",wbc,"/mL")
if(wbc<5000):
    print("Status : low")
elif(wbc>=5000 and wbc<=10000):
    print("Status : normal")
else:
    print("Status : high")
        

             
            
 
    

    
    
    
    
    
