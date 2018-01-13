import pymysql as pm
import time
from datetime import datetime as dt

def enter_grades(di):
    name = input("Student Name: ")
    Grade = input("Grades (comma sep): ").strip(" ")
    try:
        Grade = list(map(eval,Grade.split(",")))
        if(name in di):
            di[name].extend(Grade)
        else:
            di[name] = Grade
    except Exception as err:
        print ("Invalid data","not entered\n")


def remove_student(di):
    name = input("Student Name: ")
    if (name in di):
        del di[name]
        print ("Successfully removed\n")
    else:
        print ("No data found\n")


def marks_average(di):
    print ("Avg data: \n")
    if(len(di) == 0):
        print("no records found \n")
        return None
    for key in di:
        print (key,sum(di[key])/len(di[key]))
    print("\n")
        

def main():
    print ("Welcome to Grade Central")
    flag = False
    di = {}
    db = None
    file = open("log.txt","a")
    try:
        db = pm.connect("localhost","root","","user_log")
        cur = db.cursor()
        count = 1
        while not flag:
            try:
                
                Username = input("Enter Username: ")
                Password = input("Enter Password: ")
                cur.execute("SELECT PASS FROM DET WHERE USR = %s",str(Username))
                if (Password == cur.fetchall()[0][0]):
                    flag = True
                    file.write("user = "+str(Username)+" Success = YES "+" time =  "+str(dt.now())+"\n")
                    print ("logged in")
                
            except IndexError as ie:
                if(count == 5):
                           file.write("user = "+str(Username)+" Success = WAIT "+" time =  "+str(dt.now())+"\n")
                           wait = int(time.time())%100
                           print ("Waiting for some time....",wait,"Sec")
                           time.sleep(wait)
                           count = 1
                else:
                            file.write("user = "+str(Username)+" Success = NO "+" time =  "+str(dt.now())+"\n")
                            print ("Incorrect...")
                            count += 1
                            
    except Exception as err:
        if db is None:
            print ("Unable to connect ",err)
        else:
            print (err)
            db.close()
    db.close()
    file.close()
    while flag:
        print ("[1] - Enter Grades",
               "[2] - Remove Student",
               "[3] - Student Average Grades",
               "[4] - Exit",sep="\n")

        print("\nWhat Would you like to do today?",
              "(Enter a number) ",end="")

        try:
            number = int(input())
        except Exception as err:
            print ("Invalid entry \n\n")
            continue

        if(number == 1):
            enter_grades(di)

        elif(number == 2):
            remove_student(di)

        elif(number == 3):
            marks_average(di)

        elif(number == 4):
            print ("Exit \n")
            flag = False

        else:
            print ("Invalid choice \n\n")
            

if (__name__ == "__main__"):
    main()
