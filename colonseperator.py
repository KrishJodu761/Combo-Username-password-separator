count=0
passwords=open("passwords.txt", "a+") 
users=open("users.txt" , "a+")
file1=input("\nEnter the combo file name : ")
print("\n")
with open(file1) as data:
    for line in data:
        for ch in line:
            if(ch==":"):
                    passwords.write(line[line.index(ch)+1:])#Passwords will be stored in password.txt
                    users.write(line[0:line.index(ch)]+"\n")#Usernames(Email ID's) will be stored in users.txt
                    break
print("Usernames(Email Id's) stored in users.txt\n")
print("Password's stored in passwords.txt\n")
passwords.close()
users.close()
data.close()
