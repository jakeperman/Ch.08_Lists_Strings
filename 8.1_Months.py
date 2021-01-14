'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
'''
userinput = 1
while userinput <= 12 and userinput>0:
    userinput = int(input("Enter the number of the month youd like to abbreviate"))
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    print("The abbreviation for that month is:", months[(userinput * 3)-3:userinput * 3])
print("Goodbye!")

