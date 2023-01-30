import mysql.connector

def get_employees(mycursor):
    while(True):
        try:
            choice = input("Enter region name or 'ALL' : ")
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = 'SELECT * FROM EmployeesPerRegion;'
            else:
                sql_query = 'Select * FROM EmployeesPerRegion WHERE region_name = "' + choice + '";'
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: {record[1]} employees\n")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def get_mangers(mycursor):
    while(True):
        try:
            choice = input("Enter department name or 'ALL' : ")
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = '''SELECT department_name, COUNT(department_name) AS "Number of Managers"
                    FROM managers GROUP BY department_name ORDER BY COUNT(department_name) DESC;'''
            else:
                sql_query = '''SELECT department_name, COUNT(department_name) AS "Number of Managers"
                    FROM managers WHERE department_name = "''' + choice + '''" GROUP BY department_name ORDER BY COUNT(department_name) DESC;'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try: 
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: {record[1]} managers\n")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return 

def get_department_dependents(mycursor):
    while(True):
        try:
            choice = input("Enter department name or 'ALL' : ")
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = '''SELECT * FROM DependentsByDepartment;'''
            else:
                sql_query = '''SELECT * FROM DependentsByDepartment WHERE department_name = "''' + choice + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: {record[1]} dependents\n")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return 

def get_hires(mycursor):
    while(True):
        try:
            choice = input("Enter year or 'ALL' : ")
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = 'SELECT * FROM HiresByYear;'
            else:
                sql_query = '''SELECT * FROM HiresByYear WHERE year = "''' + choice + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: {record[1]} hires\n")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def get_department_salary(mycursor):
    while(True):
        try:
            choice = input("Enter department name or 'ALL' : ")
            if(choice ==  "ALL" or choice == "all" or choice == "All"):
                sql_query = 'SELECT * FROM SalaryByDepartment;'
            else:
                sql_query = '''SELECT * FROM SalaryByDepartment WHERE department_name = "''' + choice + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]} Department: ${record[1]}")
        except Exception as err:
            print(f"Error Occured: {err}")
            return   
        return

def get_job_title_salary(mycursor):
    while(True):
        try:
            choice = input("Enter job title or 'ALL' : ")
            if(choice ==  "ALL" or choice == "all" or choice == "All"):
                sql_query = 'SELECT * FROM SalaryByJobTitle;'
            else:
                sql_query = '''SELECT * FROM SalaryByJobTitle WHERE job_title = "''' + choice + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: ${record[1]}")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def get_employee_dependents(mycursor):
    while(True):
        try:
            choice = input("Enter employee first name and last name or 'ALL' : ")
            choice_edit = choice.split(' ')
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = '''SELECT * FROM EmployeeDependents;'''
            else:
                sql_query = '''SELECT * FROM EmployeeDependents WHERE first_name = "''' + choice_edit[0] + '''" AND last_name = "''' + choice_edit[1] + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]} {record[1]}: {record[4]} dependents")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return 

def get_country_locations(mycursor):
    while(True):
        try:
            choice = input("Enter country name or 'ALL' : ")
            if(choice == "ALL" or choice == "all" or choice == "All"):
                sql_query = 'SELECT * FROM CountryLocation;'
            else:
                sql_query = '''SELECT * FROM CountryLocation WHERE country_name = "''' + choice + '''";'''
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------RESULT------\n")
        try:
            mycursor.execute(sql_query)

            query_result = mycursor.fetchall()
            
            if mycursor.rowcount == 0:
                print("Failure to fetch records, please try again.")
                return
            else:
                for record in query_result:
                    print(f"{record[0]}: {record[1]} locations")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def add_dependent(mycursor):
    while(True):
        try:
            max_dep_val = "SELECT MAX(dependent_id) FROM dependents;"
            mycursor.execute(max_dep_val)
            max_query = mycursor.fetchall()
            for record in max_query:
                pull_record = f"{record[0]}"
            max_dep_id = int(pull_record)
            new_max = max_dep_id + 1
            str_max = str(new_max)
            firstname = input("Enter first name : ")
            lastname = input("Enter last name : ")
            employeeID = input("Enter employee ID : ")
            sql_query = "INSERT INTO dependents VALUES ('" + str_max  +"', '" + firstname + "', '" + lastname + "', 'Child', '" + employeeID + "');"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            show_insert = "SELECT * FROM dependents WHERE dependent_id = (SELECT MAX(dependent_id) FROM dependents);"
            print("------ INSERTED ROW ------")
            mycursor.execute(show_insert)
            query_result = mycursor.fetchall()
            print(query_result)
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def add_job(mycursor):
    while(True):
        try:
            max_job = "SELECT MAX(job_id) FROM jobs;"
            mycursor.execute(max_job)
            max_id = mycursor.fetchall()
            for record in max_id:
                pull_record = f"{record[0]}"
            max_job_id = int(pull_record)
            new_max = max_job_id + 1
            str_max = str(new_max)
            jobtitle = input("Enter job title : ")
            minsal = input("Enter minimum salary for the job : ")
            maxsal = input("Enter maximum salary for the job : ")
            sql_query = "INSERT INTO jobs VALUES ('" + str_max + "', '" + jobtitle + "', '" + minsal+ "', '" + maxsal + "');"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            show_insert = "SELECT * FROM jobs WHERE job_id = (SELECT MAX(job_id) FROM jobs);"
            print("------ INSERTED ROW ------")
            mycursor.execute(show_insert)
            query_result = mycursor.fetchall()
            print(query_result)
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def del_employee(mycursor):
    while(True):
        try:
            choice = input("Enter the first and last name of the employee you would like to delete : ")
            choice_edit = choice.split(' ')
            sql_query = "SELECT * FROM employees WHERE first_name = '" + choice_edit[0] + "' AND last_name = '" + choice_edit[1] + "';"
            del_query = "DELETE FROM employees WHERE first_name = '" + choice_edit[0] + "' AND last_name = '" + choice_edit[1] + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch employee, please try again.")
                return
            else:
                mycursor.execute(del_query)
                print(choice + " has been removed from the employees table.")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def del_dependent(mycursor):
    while(True):
        try:
            choice = input("Enter the first and last name of the dependent you would like deleted : ")
            choice_edit = choice.split(' ')
            sql_query = "SELECT * FROM dependents WHERE first_name = '" + choice_edit[0] + "' AND last_name = '" + choice_edit[1] + "';"
            del_query = "DELETE FROM dependents WHERE first_name = '" + choice_edit[0] + "' AND last_name = '" + choice_edit[1] + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch dependent, please try again.")
                return
            else:
                mycursor.execute(del_query)
                print(choice + " has been removed from the dependents table.")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def upd_emp_fname(mycursor):
    while(True):
        try:
            emp_id = input("Enter the employee ID number of the employee you would like to update : ")
            new_emp_name = input("Enter the updated first name : ")
            upd_query = "UPDATE employees SET first_name = '" + new_emp_name + "' WHERE employee_id = '" + emp_id + "';"
            sql_query = "SELECT * FROM employees WHERE employee_id = '" + emp_id + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch employee, please try again.")
                return
            else:
                mycursor.execute(upd_query)
                result_query = "SELECT first_name FROM employees WHERE employee_id = '" + emp_id + "';"
                mycursor.execute(result_query)
                update = mycursor.fetchall()
                for result in update:
                    print("The first name of employee ID: " + emp_id + f" is now {result[0]}.") 
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def upd_emp_lname(mycursor):
    while(True):
        try:
            emp_id = input("Enter the employee ID number of the employee you would like to update : ")
            new_emp_name = input("Enter the updated last name : ")
            sql_query = "UPDATE employees SET last_name = '" + new_emp_name + "' WHERE employee_id = '" + emp_id + "';"
            test_query = "SELECT * FROM employees WHERE employee_id = '" + emp_id + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(test_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch employee, please try again.")
                return
            else:
                mycursor.execute(sql_query)
                result_query = "SELECT last_name FROM employees WHERE employee_id = '" + emp_id + "';"
                mycursor.execute(result_query)
                update = mycursor.fetchall()
                for result in update:
                    print("The last name of employee ID: " + emp_id + f" is now {result[0]}.")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return


def upd_job_min_sal(mycursor):
    while(True):
        try:
            job_id = input("Enter the job ID you would like to update : ")
            new_sal = input("Enter the adjusted minimum salary : ")
            upd_query = "UPDATE jobs SET min_salary = '" + new_sal + "' WHERE job_id = '" + job_id + "';"
            sql_query = "SELECT * FROM jobs WHERE job_id = '" + job_id + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch job ID, please try again.")
                return
            else:
                mycursor.execute(upd_query)
                result_query = "SELECT job_title, min_salary FROM jobs WHERE job_id = '" + job_id + "';"
                mycursor.execute(result_query)
                update = mycursor.fetchall()
                for result in update:
                    print(f"The minimum salary of job '{result[0]}' is now {result[1]}.")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return

def upd_job_max_sal(mycursor):
    while(True):
        try:
            job_id = input("Enter the job ID you would like to update : ")
            new_sal = input("Enter the adjusted maximum salary : ")
            upd_query = "UPDATE jobs SET max_salary = '" + new_sal + "' WHERE job_id = '" + job_id + "';"
            sql_query = "SELECT * FROM jobs WHERE job_id = '" + job_id + "';"
        except Exception as err:
            print(f"Error Occured: {err}")
            continue
        print("\n------ RESULT ------\n")
        try:
            mycursor.execute(sql_query)
            mycursor.fetchall()
            if mycursor.rowcount == 0:
                print("Failure to fetch job ID, please try again.")
                return
            else:
                mycursor.execute(upd_query)
                result_query = "SELECT job_title, max_salary FROM jobs WHERE job_id = '" + job_id + "';"
                mycursor.execute(result_query)
                update = mycursor.fetchall()
                for result in update:
                    print(f"The maximum salary of job '{result[0]}' is now {result[1]}.")
        except Exception as err:
            print(f"Error Occured: {err}")
            return
        return


def print_menu():
    print("\nVIEW DATA\n-----------------------")
    print("1. View employees data per region")
    print("2. View manager count by department")
    print("3. View dependent data per department")
    print("4. Show hiring data by year")
    print("5. View salary data by department")
    print("6. View salary data by job title")
    print("7. View dependent data by employee")
    print("8. View location data by country")
    print("\nADD DATA\n-----------------------")
    print('9. Add a dependent')
    print('10. Add a job')
    print("\nDELETE DATA\n-----------------------")
    print('11. Delete an employee')
    print('12. Delete a dependent')
    print("\nUPDATE DATA\n-----------------------")
    print('13. Update employee first name')
    print('14. Update employee last name')
    print('15. Update job minimum salary')
    print('16. Update job maximum salary')
    print("\nEXIT\n-----------------------")
    print("17. Exit Application")
    return

def get_user_choice():
    print_menu()
    while(True):
        try:
            menu_choice = int(input("Enter Choice: "))
            if(menu_choice < 1 or menu_choice > 17):
                print(f"Invalid input: Enter a value between 1 and 17.\n")
                continue
            break
        except Exception as err:
            print(f"An error has occured: {err}\n")
            continue

    return menu_choice

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        user_choice = get_user_choice()
        if(user_choice == 1):
            get_employees(mycursor)
        elif(user_choice == 2):
            get_mangers(mycursor)
        elif(user_choice == 3):
            get_department_dependents(mycursor)
        elif(user_choice == 4):
            get_hires(mycursor)
        elif(user_choice == 5):
            get_department_salary(mycursor)
        elif(user_choice == 6):
            get_job_title_salary(mycursor)
        elif(user_choice == 7):
            get_employee_dependents(mycursor)
        elif(user_choice == 8):
            get_country_locations(mycursor)
        elif(user_choice == 9):
            add_dependent(mycursor)
            mydb.commit()
        elif(user_choice == 10):
            add_job(mycursor)
            mydb.commit()
        elif(user_choice == 11):
            del_employee(mycursor)
            mydb.commit()
        elif(user_choice == 12):
            del_dependent(mycursor)
            mydb.commit()
        elif(user_choice == 13):
            upd_emp_fname(mycursor)
            mydb.commit()
        elif(user_choice == 14):
            upd_emp_lname(mycursor)
            mydb.commit()
        elif(user_choice == 15):
            upd_job_min_sal(mycursor)
            mydb.commit()
        elif(user_choice == 16):
            upd_job_max_sal(mycursor)
            mydb.commit()
        elif(user_choice == 17):
            print("Bye Bye!!!")
            break

main()