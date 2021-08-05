import sqlite3

class CsuData:

 def create_student_table(): #Create table function
    connect = sqlite3.connect('universitystudent.db') # Connect to the database
    cursor = connect.cursor() #Get the cursor
    DB_CREATE_STUDENT_TABLE = 'CREATE TABLE IF NOT EXISTS student(student_id VARCHAR(243) PRIMARY KEY,student_name VARCHAR(243),student_phone VARCHAR(243) ,student_enrollment_status VARCHAR(243) ,student_department_id VARCHAR(243));' 
    cursor.executescript(DB_CREATE_STUDENT_TABLE)
    connect.commit()#Close the database
    cursor.close()
    connect.close()

 def add_student(): 
    student_id = input('Please enter the student_id')
    student_name = input('Please enter the student_name')
    student_phone = input('Please enter the student_phone:')
    student_enrollment_status = input('Please enter student_enrollment_status')
    student_department_id = input('Please enter student_department_id')
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = 'INSERT INTO student(student_id, student_name, student_phone, student_enrollment_status,student_department_id) VALUES (:student_id, :student_name, :student_phone,:student_enrollment_status, :student_department_id);'
    cursor.execute(sql,{'student_id':student_id,'student_name':student_name,'student_phone':student_phone,'student_enrollment_status':student_enrollment_status,'student_department_id':student_department_id })
    connect.commit()
    connect.close()
    print('Student Information Add Complete')    

 def show_student_table():
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_STUDENT_TABLE = 'SELECT * FROM student'
    cursor.execute(DB_SELECT_STUDENT_TABLE) 
    student_list = cursor.fetchall()
    print(student_list)
    connect.commit()
    cursor.close()
    connect.close()     

 def create_account_table(): #Create table function
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_CREATE_ACCOUNT_TABLE = 'CREATE TABLE IF NOT EXISTS account(account_id VARCHAR(243) PRIMARY KEY,account_balance NUMBER,account_status VARCHAR(243),student_id VARCHAR(243) ,FOREIGN KEY(student_id) REFERENCES student(student_id));'
    cursor.executescript(DB_CREATE_ACCOUNT_TABLE)
    connect.commit()#Close the database
    cursor.close()
    connect.close() 

 def add_account_table(): 
    account_id = input('Please enter the account_id')
    account_balance = input('Please enter the account_balance')
    student_id = input('Please enter the student_id:')
    account_status = input('Please enter account_status')
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = "INSERT INTO account(account_id, account_balance, account_status, student_id) VALUES (:account_id, :account_balance, :account_status,:student_id);"
    cursor.execute(sql,{'account_id':account_id, 'account_balance':account_balance,'account_status':account_status, 'student_id':student_id})
    connect.commit()
    connect.close()
    print('Account Information Add Complete')    

 def show_account_balance(self, inp):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_ACCOUNT_TABLE = 'SELECT * FROM account where student_id '
    cursor.execute(DB_SELECT_ACCOUNT_TABLE)
    account_list = cursor.fetchall()
    account_balance = 0;
    for index, account in enumerate(account_list): 
     if account[3] == inp:
        account_balance = account[1];
    connect.commit()
    cursor.close()
    connect.close()   
    return account_balance  


 def show_full_billing_table():
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_ACCOUNT_TABLE = 'SELECT * FROM account'
    cursor.execute(DB_SELECT_ACCOUNT_TABLE)
    account_list = cursor.fetchall()
    for index, account in enumerate(account_list): 
     print(account_list)
    connect.commit()
    cursor.close()
    connect.close()
         

 def create_payments_table(): #Create table function
    connect = sqlite3.connect('universitystudent.db') # Connect to the database
    cursor = connect.cursor() #Get the cursor
    DB_CREATE_PAYMENTS_TABLE = 'CREATE TABLE IF NOT EXISTS payment(payment_id VARCHAR PRIMARY KEY,payment_method VARCHAR ,payment_amount NUMBER ,student_id VARCHAR,FOREIGN KEY(student_id) REFERENCES student(student_id));'
    cursor.execute(DB_CREATE_PAYMENTS_TABLE)
    connect.commit()#Close the database
    cursor.close()
    connect.close()

 def add_payments_table(): 
    payment_id = input('Please enter the payment_id')
    payment_method = input('Please enter the payment_method')
    payment_amount = input('Please enter the payment_amount')
    student_id = input('Please enter the student_id')
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = "INSERT INTO payment(payment_id, payment_method, payment_amount, student_id) VALUES (:payment_id, :payment_method,:payment_amount,:student_id);"
    cursor.execute(sql,{'payment_id':payment_id, 'payment_method':payment_method,'payment_amount':payment_amount, 'student_id':student_id })
    connect.commit()
    connect.close()
    print('payment Information Add Complete')    

 def show_payments_table(self, inp):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_STUDENT_TABLE = 'SELECT * FROM payment'
    cursor.execute(DB_SELECT_STUDENT_TABLE)
    payment_list = cursor.fetchall()
    payment_method = ""
    payment_amount = 0
    for index, payment in enumerate(payment_list):
     if payment[3] == inp:
        payment_method = payment[1]
        payment_amount = payment[2]
    connect.commit()
    cursor.close()
    connect.close()    
    return  payment_method,payment_amount 

 def show_full_payments_table():
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_UPDATE_PAYMENT_TABLE = 'UPDATE payment SET payment_amount = ? ,payment_method = ?  WHERE student_id = ? ;'
    cursor.execute(DB_UPDATE_PAYMENT_TABLE, ('3000','debit','900777634',))
    DB_SELECT_PAYMENT_TABLE = 'SELECT * FROM payment'
    cursor.execute(DB_SELECT_PAYMENT_TABLE)
    payment_list = cursor.fetchall()
    for index, payment in enumerate(payment_list):
      print(payment_list)
    connect.commit()
    cursor.close()
    connect.close()      

 def create_course_table(): #Create table function
    connect = sqlite3.connect('universitystudent.db') # Connect to the database
    cursor = connect.cursor() #Get the cursor
    DB_CREATE_COURSE_TABLE = 'CREATE TABLE IF NOT EXISTS course(course_id VARCHAR(243) PRIMARY KEY ,course_name VARCHAR NOT NULL, course_schedue VARCHAR NOT NULL, course_semester VARCHAR NOT NULL);'
    cursor.executescript(DB_CREATE_COURSE_TABLE)
    connect.commit()#Close the database
    cursor.close()
    connect.close() 

 def add_course_table(): 
    course_id = input('Please enter the course id ')
    course_name = input('Please enter the course name')
    course_schedue = input('Please enter the course scheduled')
    course_semester = input('Please enter the semester')
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = "INSERT INTO course(course_id, course_name, course_schedue, course_semester) VALUES (:course_id, :course_name, :course_schedue, :course_semester);"
    cursor.execute(sql, {'course_id':course_id, 'course_name':course_name, 'course_schedue':course_schedue, 'course_semester': course_semester})
    connect.commit()
    connect.close()
    print('Course Information Add Complete')    

 def show_course_table(self, inp):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_COURSE_TABLE = 'SELECT * FROM course'
    cursor.execute(DB_SELECT_COURSE_TABLE)
    course_list = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()    
    return  course_list    


 def show_full_course_table():
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_COURSE_TABLE = 'SELECT * FROM course'
    cursor.execute(DB_SELECT_COURSE_TABLE)
    course_list = cursor.fetchall()
    print(course_list)
    connect.commit()
    cursor.close()
    connect.close()    
    return  course_list   

 def update_full_course_table():
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_UPDATE_COURSE_TABLE = 'UPDATE course SET course_semester = ? WHERE course_id = ? ;'
    cursor.execute(DB_UPDATE_COURSE_TABLE, ('Spring-2021','10002',))
    DB_SELECT_COURSE_TABLE = 'SELECT * FROM course'
    cursor.execute(DB_SELECT_COURSE_TABLE)
    course_list = cursor.fetchall()
    print(course_list)
    connect.commit()
    cursor.close()
    connect.close()    
    return  course_list         

 def create_student_course_table(): #Create table function
    connect = sqlite3.connect('universitystudent.db') # Connect to the database
    cursor = connect.cursor() #Get the cursor
    DB_CREATE_COURSE_TABLE = 'CREATE TABLE IF NOT EXISTS student_course(student_course_id VARCHAR(243) PRIMARY KEY , student_id VARCHAR(243) NOT NULL, course_id VARCHAR(243) NOT NULL, grade VARCHAR(243) NOT NULL, course_semester VARCHAR(243) NOT NULL, FOREIGN KEY(student_id) REFERENCES student(student_id), FOREIGN KEY(course_id) REFERENCES course(course_id));'
    cursor.executescript(DB_CREATE_COURSE_TABLE)
    connect.commit()#Close the database
    cursor.close()
    connect.close()

 def add_student_course_table(): 
    student_course_id = input('Please enter the student_course_id')
    student_id = input('Please enter the student_id')
    course_id = input('Please enter the course_id')
    grade = input('Please enter the grade')
    course_semester = input('Please enter the semester')
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = 'INSERT INTO student_course(student_course_id, student_id, course_id, grade, course_semester) VALUES (:student_course_id, :student_id,:course_id,:grade, :course_semester);'
    cursor.execute(sql,{'student_course_id':student_course_id, 'student_id':student_id,'course_id':course_id, 'grade':grade, 'course_semester':course_semester })
    connect.commit()
    connect.close()
    print('Student Course Information Add Complete') 



 def show_full_student_course_table(): 
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    sql = 'SELECT * FROM  student_course'
    cursor.execute(sql)
    student_course_list = cursor.fetchall()
    print(student_course_list)
    connect.commit()
    connect.close()
    print('Student Course Information Add Complete')    


 def show_registered_courses(self,csuId,semester):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_STUDENT_COURSE_TABLE = "SELECT * FROM course where course_id IN (SELECT course_id FROM  student_course  where student_id=? and course_semester=?)"
    cursor.execute(DB_SELECT_STUDENT_COURSE_TABLE,(csuId,semester,))
    student_course_list = cursor.fetchall()
    registered_courses = []
    for index, student_course in enumerate(student_course_list):
        course_name = student_course[1]
        course_semester_info = student_course[3]
        args = {
                'id' : index,
                'course_name': course_name,
                'course_semester': course_semester_info
        }
        registered_courses.append(args)   
    connect.commit()
    cursor.close()
    connect.close()
    return registered_courses


 def show_course_schedules(self,semester):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_COURSE_TABLE = 'SELECT * FROM course where course_semester=?;'
    cursor.execute(DB_SELECT_COURSE_TABLE, (semester,))
    course_list = cursor.fetchall()
    course_schedue = []
    for index, course in enumerate(course_list):
        args = {
                'id' : index,
                'course_name': course[1],
                'course_semester': course[2]
        }
        course_schedue.append(args)
    connect.commit()
    cursor.close()
    connect.close()
    return course_schedue 

 def show_latest_transcripts(self,csuId,semester):
    connect = sqlite3.connect('universitystudent.db')
    cursor = connect.cursor()
    DB_SELECT_TRANSCRIPTS_TABLE = "SELECT * FROM student_course INNER JOIN course ON student_course.course_id=course.course_id where student_id=?"
    cursor.execute(DB_SELECT_TRANSCRIPTS_TABLE, (csuId,))
    student_course_list = cursor.fetchall()
    transcripts = []
    for index, student_course in enumerate(student_course_list):
        args = {
                'id' : index,
                'course_name': student_course[6],
                'course_grade': student_course[3]
        }
        transcripts.append(args)
    connect.commit()
    cursor.close()
    connect.close() 
    return transcripts


 def main():
         # function, program entry
    while True:
        print("""
                 ******** Welcome to the student management system **********
                           * 1-Create student table *
                           * 2-Add student data *
                           * 3-view student data *
                           * 4-Create account table *
                           * 5-Add account data *
                           * 6-view account data *
                           * 7-Create payments table *
                           * 8-Add payment data *
                           * 9-view payment data *
                           * 10-create_course_table *
                           * 11-add_course_table*
                           * 12-create_student_course_table*
            """)

        num = input('Please enter the operation number: ')
        if not num.isdigit():
            print("The input must be a number!!!")
            continue
        num = int(num)
        if num == 1:
            create_student_table()
        elif num == 2:
            add_student()
        elif num == 3:
            show_student_table()
        elif num == 4:
            create_account_table()
        elif num == 5:
            add_account_table()   
        elif num == 6:
            show_account_balance()
        elif num == 7:
            create_payments_table()
        elif num == 8:
            add_payments_table()   
        elif num == 9:
            show_payments_table() 
        elif num == 10:
            create_course_table()
        elif num == 11:
            add_course_table()   
        elif num == 12:
            create_student_course_table()   
        elif num == 13:
            add_student_course_table()
        elif num == 14:
            show_registered_courses()   
        elif num == 15:
            show_course_schedules()
        elif num == 16:
            show_latest_transcripts() 
        elif num == 17:
            show_course_table() 
        elif num == 18:
            show_full_course_table()  
        elif num == 19:
            show_full_billing_table() 
        elif num == 20:
            show_full_student_course_table() 
        elif num == 21:
            show_full_account_table()  
        elif num == 22:
            update_full_course_table() 
        elif num == 23:
            show_full_payments_table()                                        
        elif num == 0:
            break
        else:
            print('The input is incorrect, please re-select!')
        continue

if __name__=='__main__':
    main()