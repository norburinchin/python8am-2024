# print("==============Nepal Telecome===============")
# print("1. NTC to NTC (Rs:2.5)")
# print("2. NTC to Ncell(Rs:3.5)")
# print("3. Ncell to NTC(RS: 4.5)")
# print("4. Ncell to Ncell(Rs: 5.5)")

# option= int(input("Enter your choice:"))
# if option==1:
#     call_duration = int(input("Enter the call duration:"))
#     if call_duration>1 and call_duration<10:
#         print(f"your bonus",2.5)
#     elif call_duration>10 and call_duration<20:
#         print(f"Your bonus", 5)
#     elif call_duration>20 and call_duration<30:
#         print(f"Your bonus",7.5)
# elif option==2:
#     pass
# elif option==3:
#     pass
# elif option==4:
#     pass



"====================Bus far================"
print("1.Kalanki to Swyambhu 5km(Rs:15)")
print("2. kanlanki to buspark 10km(Rs:30)")
print("3.kalanki to chakrapath15km(Rs:45)")
print("4.kalani to chabahil 20K(Rs:60.)")
print("5.kalanki to boudha 27k(Rs:75)")

option= int(input("Enter your choice:"))

if option==1:
    transport_duration= int(input("enter the transport duration:"))
    if transport_duration>1 and transport_duration<5:
        print("Your fare is",15)
    elif transport_duration>5 and transport_duration<10:
        print("Your fare is ",30)
    elif transport_duration>10 and transport_duration<15:
        print("your fare is",45)
    
    elif transport_duration>15 and transport_duration<20:
        print("Your fare is ",60)
    else:
        print("Your dare is",75)

                
   
   


