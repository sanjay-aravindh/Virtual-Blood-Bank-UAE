##PROJECT FILE


#Introduction

print("HI THERE!")
print(" ")
print(" ")
print("Welcome to Virtual Blood Bank!")
print(" ")
print(" ")

import mysql.connector
mydb = mysql.connector.connect(host = "localhost",\
                               user = "root",\
                               password = "star",\
                               database = "PracticalFile")

cursor = mydb.cursor()


# Creating Blood Unit Table

try:
    cursor.execute('''
CREATE TABLE BloodUnits(BLOOD_GROUP varchar(20), AMOUNT_ml int);
''')
except:
    pass

# Inserting data into Blood Unit Table
blood_unit_data = [
    ('O-', 1000),
    ('O+', 3000),
    ('A-', 6500),
    ('A+', 7500),
    ('B-', 3600),
    ('B+', 8900),
    ('AB-', 2000),
    ('AB+', 980)
]

try:
    cursor.executemany("INSERT INTO BloodUnits VALUES (%s, %s)", blood_unit_data)
except:
    pass


#Creating Donor Details Table
try:
    cursor.execute('''
CREATE TABLE `DONOR_DETAILS`(`ID` INT NOT NULL,PRIMARY KEY (`ID`), D_NAME varchar(20), CONTACT_NO varchar(20), BLOOD_GROUP varchar(20), AMOUNT_ml int);
''')
except:
    pass

# Inserting data into Donor Details Table
donor_data = [
    (1, 'Omkara', '0566140526', 'O+', 450),
    (2, 'Gauri', '0566140736', 'AB+', 360),
    (3, 'Anika', '9386140526', 'AB-', 400),
    (4, 'Rudra', '0386193526', 'B+', 470),
    (5, 'Shivaay', '0266183656', 'AB-', 350),
    (6, 'Bhavya', '8364140526', 'B-', 470)
]
try:
    cursor.executemany("INSERT INTO DONOR_DETAILS VALUES (%s, %s, %s, %s, %s)", donor_data)
except:
    pass


# Creating Receiver Details Table
try:
    cursor.execute('''
CREATE TABLE RECEIVER_DETAILS (R_NAME varchar(20), CONTACT_NO varchar(20), BLOOD_GROUP varchar(20), STATUS varchar(20));
''')
except:
    pass

# Inserting data into Receiver Details Table
receiver_data = [('Abhay', '0566140846', 'O+', 'Pending')]
try:
    cursor.executemany("INSERT INTO RECEIVER_DETAILS VALUES (%s, %s, %s, %s)", receiver_data)
except:
    pass


# Creating Location Table
try:
    cursor.execute('''
CREATE TABLE LOCATION (EMIRATE varchar(20), B_BANK varchar(100));
''')
except:
    pass

# Inserting data into Location Table
location_data = [
    ('Abu Dhabi', 'Blood Bank - Zayed Military Hospital'),
    ('Abu Dhabi', 'Abu Dhabi Blood Bank Center'),
    ('Dubai', 'Blood Bank - Latifa Hospital'),
    ('Dubai', 'Blood Bank - Al Baraha Hospital'),
    ('Sharjah', 'Sharjah Blood Transfusion and Research Center'),
    ('Ajman', 'Blood Bank - Ajman Khalifa Hospital'),
    ('Umm-Al-Quwain', 'Blood Bank - Umm Al Quwain Hospital'),
    ('Ras-Al-Khaimah', 'Blood Bank - Saqar Hospital'),
    ('Ras-Al-Khaimah', 'Blood Bank – Saif Bin Gubash Hospital'),
    ('Fujairah', 'Blood Bank - Fujairah Hospital'),
    ('Fujairah', 'Blood Bank - Dibba Al Fujairah Hospital'),
    ('AlAin', 'Blood Bank - Al Ain Hospital')
]
try:
    cursor.executemany("INSERT INTO LOCATION VALUES (%s, %s)", location_data)
except:
    pass

mydb.commit()


##FUNCTIONS

#DISPLAY FUNCTIONS

# Function to display Blood Unit Table
def display_units():
    cursor.execute("SELECT DISTINCT * FROM BloodUnits")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to display Donor Table
def display_donor():
    cursor.execute("SELECT DISTINCT * FROM DONOR_DETAILS")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to display Receiver Table
def display_receiver():
    cursor.execute("SELECT  DISTINCT * FROM RECEIVER_DETAILS")
    result = cursor.fetchall()
    for row in result:
        print(row)


#TO ADD RECORD
        
#Function to add Donor Details to Database
def donor_details(d_id, name, contact, btype, aml):
    cursor.execute("INSERT INTO DONOR_DETAILS VALUES (%s, %s, %s, %s, %s);", (d_id, name, contact, btype, aml))

#Function to add Receiver Details to Database
def receiver_details(rname, phnum, bgroup, status):
    cursor.execute("INSERT INTO RECEIVER_DETAILS VALUES (%s, %s, %s, %s);", (rname, phnum, bgroup, status))


#ALTER RECORDS

# Function to alter Blood Unit Table
def alter_bunit(bgroup, amount):
    cursor.execute('''
        UPDATE BloodUnits
        SET AMOUNT_ml = %s
        WHERE BLOOD_GROUP = %s
    ''', (amount, bgroup))

# Function to alter Donor Details Table
def alter_donor(amount, dname):
    
    cursor.execute('''
    ALTER TABLE DONOR_DETAILS
    ADD PRIMARY KEY (D_NAME)
    ''')

# Function to alter Receiver Table
def alter_receiver(stat, rname):
    cursor.execute('''
        UPDATE RECEIVER_DETAILS
        SET STATUS = %s
        WHERE R_NAME = %s
    ''', (stat, rname))


#DELETE RECORD

#Function to delete record in Donor Table
def delete_donor(don_id):
    cursor.execute("DELETE FROM DONOR_DETAILS WHERE id = %s", (don_id,))

#Function to delete record in Receiver Table
def delete_receiver(rec_name):
    cursor.execute("DELETE FROM RECEIVER_DETAILS WHERE R_NAME = %s", (rec_name,))


choice = 0
while True:
    print("Here's your Directory:")
    print(" ")
    print("1.Admin Login")
    print("2.Eligibility and Requirements for Blood Donation")
    print("3.Donor Registration")
    print("4.View Donor Details")
    print("5.Receiver Requestion")
    print("6.Receiver Status")
    print("7.Find your Nearest Blood Bank")
    print("8.Exit")
    print(" ")
    choice = int(input("Enter your Choice: "))
    print(" ")
    print(" ")

    if choice == 1:
        print("Welcome to Admin Login!")
        print(" ")
    
        admin_password="admin@123"
        password = input("Enter Admin Password: ")
    
        if password == admin_password:
            print("Login Successful!")
            while True:
                print(" ")
                print("Admin Directory:")
                print("1. View Blood Unit Table")
                print("2. View Donor Table")
                print("3. Reciever Table")
                print("4. Add Donor Details")
                print("5. Update Receiver Status")
                print("6. Delete Donor Record")
                print("7. Delete Receiver Record")
                print("8. Exit")
                print(" ")
                a = int(input("Enter your Choice: "))
                print(" ")
                
                if a == 1:
                    display_units()
                    print(" ")

                elif a == 2:
                    display_donor()
                    print(" ")

                elif a == 3:
                    display_receiver()
                    print(" ")

                elif a == 4:
                    while True:
                        f = int(input("Enter giver Donor ID: "))
                        cursor.execute("SELECT COUNT(*) FROM DONOR_DETAILS WHERE ID = %s", (f,))
                        if cursor.fetchone()[0]>0:
                            print("Error: Donor ID",f," has already been registered. Please enter a different ID.")
                        else:
                            break
                    b = input("Enter First Name: ")
                    c = int(input("Enter your Contact Number: "))
                    d = input("Enter your Blood Type: ")
                    e = int(input("Enter Amount of Blood Donated: "))
                    donor_details(f, b, c, d, e)
                    print("Donor successfully registered!")
                    print(" ")
                    print(" ")
    
                elif a == 5:
                    g = input("Enter Status: ")
                    h = input("Enter Receiver's Name: ")
                    alter_receiver(g, h)
                    print("Status Updated!")
                    print(" ")
                    print(" ")

                elif a == 6:
                    i = int(input("Enter Donor ID: "))
                    delete_donor(i)
                    print("Record Deleted!")
                    print(" ")
                    print(" ")

                elif a == 7:
                    j = input("Enter Receiver Name: ")
                    delete_receiver(j)
                    print("Record Deleted!")
                    print(" ")
                    print(" ")

                elif a == 8:
                    break

                else:
                    print("Incorrect Option")
                    print(" ")
                    print(" ")
        else:
            print("Incorrect password! Access denied.")
            
                      
    elif choice==2:
        print('''        
Before your blood donation:

Get plenty of sleep the night before you plan to donate.
Eat a healthy meal before your donation.
Drink plenty of water before the donation.
Check to see if any medications you are taking.

After your blood donation:

Drink extra fluids.
Avoid strenuous physical activity or heavy lifting for about five hours.
If you feel lightheaded, lie down with your feet up until the feeling passes.
Keep your bandage on and dry for the next five hours.
If you have bleeding after removing the bandage, put pressure on the site.
Consider adding iron-rich foods to your diet.
''')
        print(" ")
        print(" ")

    elif choice == 3:
        print("Welcome to Donor Registration")
        print(" ")
    
        while True:
            f = int(input("Enter giver Donor ID: "))
        
        
            cursor.execute("SELECT COUNT(*) FROM DONOR_DETAILS WHERE ID = %s", (f,))
            if cursor.fetchone()[0] > 0:
                print("Error: Donor ID",f," has already been registered. Please enter a different ID.")
            else:
                break
        b = input("Enter First Name: ")
        c = int(input("Enter your Contact Number: "))
        d = input("Enter your Blood Type: ")
        e = int(input("Enter Amount of Blood Donated: "))
        donor_details(f, b, c, d, e)
        print("Donor successfully registered!")
        print(" ")
        print(" ")

    elif choice == 4:
        try:
            k = int(input("Enter Donor ID: "))
            cursor.execute("SELECT * FROM DONOR_DETAILS WHERE ID = %s;", (k,))
            data = cursor.fetchall()

            if data:
                for row in data:
                    print(row)
                    print(" ")
                    print(" ")
            else:
                print("No records found for Donor ID:", k)

        except ValueError:
            print("Invalid input. Please enter a valid integer for Donor ID.")
        except Exception as e:
            print("An error occurred:", str(e))
            


    elif choice == 5:
        try:
            print("Fill in the following Details:")
            print(" ")
            m = input("Enter your Name: ")
            n = int(input("Enter your Contact Number: "))
            o = input("Enter your Blood Group: ")
            p = "Pending"
            receiver_details(m, n, o, p)
            print("Your request has been recorded!")
            print(" ")
            print("Enter 6 to check status")
            print(" ")
            print(" ")

        except ValueError:
            print("Invalid input. Please enter a valid integer for Contact Number.")
        except Exception as e:
            print("An error occurred:", str(e))

    elif choice == 6:
        q = input("Enter your Name: ")
        cursor.execute("SELECT STATUS FROM RECEIVER_DETAILS WHERE R_NAME = %s;", (q,))

    elif choice == 7:
        em = input("Enter Emirate: ")
        print(" ")
        print("Your Nearest Blood Banks:")
        cursor.execute("SELECT * FROM LOCATION where EMIRATE = %s", (em,))
        records = cursor.fetchall()
        print(records)
      
    elif choice == 8:
        print("The Greatest Wealth is Health!")
        print(" ")
        print(" ")
        break

    else:
        print("Enter a Valid Choice!")
        print(" ")
        print(" ")

print("BYE!")
