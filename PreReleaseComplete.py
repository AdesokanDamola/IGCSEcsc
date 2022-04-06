from datetime import datetime, date

#TASK 1 --- becoming a member of Friends of Seaview Pier
FirstName = []
LastName = []
VoluntChoice = []
ChoosenArea = []
JoinDate = []
Payment = []
VoluntArea = ['Pier entrance gate', 'Gift Shop','Painting and Decorating']
SponsorChoice = []
SponsorFName = []
SponsorLName = []
SponsorMsg = []


while (True):
    MemberChoice = input('\nEnter "YES" to enrol as a member of Friends of Seaview Pier or "No" to quit.\n')
    MemberChoice = MemberChoice.upper()
    while MemberChoice != "YES" and MemberChoice != "NO":
            MemberChoice = input('Invalid Input! Please enter "YES" or "NO" \n')
            MemberChoice = MemberChoice.upper()

    if MemberChoice =='NO':
        break   
            
    FName = input('\nEnter your first name: ')
    FirstName.append(FName)
    LName = input('\nEnter your last name: ')
    LastName.append(LName)
    
    VChoice = input("\nWould you like to work as a volunteer? \n Enter 'YES' or 'NO' \n")
    VChoice = VChoice.upper()
    while VChoice != "YES" and VChoice != "NO":
        VChoice = input('\nInvalid Input! Please enter "YES" or "NO" \n')
        VChoice = VChoice.upper()
    VoluntChoice.append(VChoice)
    
    if VChoice == 'YES':
        print('\nIdentify your volunteer area')
        for Area in range (len(VoluntArea)):
            print('Enter ', Area+1, ' to volunteer at ', VoluntArea[Area])
        VArea =int(input('\n'))
        while VArea < 1 or VArea >3:
            VArea = int(input('Invalid Input! Please enter "1", "2", or "3" \n'))
        ChoosenArea.append(VArea)
    
    print("\nWhen did you join 'Friends of Seaview Pier?")
    Now = date.today()
    CorrectDate = False
    JDate = input("Enter your join date e.g. DD/MM/YYYY: \n")

    
    while CorrectDate == False:
        try:
          DateCheck = datetime.strptime(JDate, "%d/%m/%Y").date()
          CorrectDate = True
        except ValueError:
            JDate = input("Incorrect data format! DD/MM/YYYY")
    JoinDate.append(DateCheck)
    
    print('\nHave you paid your $75 committment fee?')
    Pay = input("Enter 'YES' or 'NO': \n ")
    Pay = Pay.upper()
    while Pay != "YES" and Pay != "NO":
        Pay = input('\nInvalid Input! Please enter "YES" or "NO" \n')
        Pay = Pay.upper()
    Payment.append(Pay)


    #......................TASK 3................................
    SponsChoice = input("\nwould you like to sponsor the pier’s wooden planks? Enter 'YES' or 'NO'\n")
    SponsChoice = SponsChoice.upper()
    while SponsChoice != "YES" and SponsChoice != "NO":
            SponsChoice = input('Invalid Input! Please enter "YES" or "NO" \n')
            SponsChoice = SponsChoice.upper()
    SponsorChoice.append(SponsChoice)

    if SponsChoice =="YES":
        Confirm = False
        while Confirm == False:
            FName = input('\nEnter your first name: \n')
            LName = input('\nEnter your last name: \n')
            msg = input("\nWrite a short messages you would like to have on your brass plaque.\n")
            print("\n......Confirm your details......")
            print('First Name:', FName, " ", 'Last Name:', LName, "\n",'Messsage:', msg)
            Check = input("\nConfirm if your input is correct. Enter 'YES' or 'NO'\n")
            Check=Check.upper()
            while Check != "YES" and Check != "NO":
                Check = input('Invalid Input! Please enter "YES" or "NO" \n')
                Check = Check.upper()
            if Check =="YES":
                Confirm = True
                
        SponsorFName.append(FName)
        SponsorLName.append(LName)
        SponsorMsg.append(msg)

    
#Task 2 – using the membership data
print('\nMembers who have chosen to work as volunteers')
serial = 0
for member in range (len(VoluntChoice)):
    if VoluntChoice[member] == "YES":
        serial +=1
        print(serial, FirstName[member], ' ', LastName[member])

print('\nVolunteers at the pier entrance gate')
for member in range(len(ChoosenArea)):
    if ChoosenArea[member] == 1:
        print(FirstName[member], ' ', LastName[member])    

print('\nVolunteers at the gift shop')
for member in range(len(ChoosenArea)):
    if ChoosenArea[member] == 2:
        print(FirstName[member], ' ', LastName[member])

print('\nVolunteers to help with painting and decorating')
for member in range(len(ChoosenArea)):
    if ChoosenArea[member] == 3:    
        print(FirstName[member], ' ', LastName[member])

print("\nMembers whose membership has expired")
for date in range(len(JoinDate)):
    DateDiff = Now - JoinDate[date]
    if DateDiff.days >=365:
        print(FirstName[date], LastName[date])

print('\nMembers who have not yet paid their $75 fee')
for pay in range (len(Payment)):
    if Payment[pay] =='NO':
        print(FirstName[pay], ' ', LastName[pay])
        
