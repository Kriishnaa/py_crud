import mysql.connector

# MySQL connection setup
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test_db"
)

cursor = connection.cursor()

# Function to create a new employee record
def create_employee(name, age, department):
    sql = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
    val = (name, age, department)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee {name} added successfully!")

# Function to read all employee records
def read_employees():
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update an employee record by ID
def update_employee(employee_id, name, age, department):
    sql = "UPDATE employees SET name=%s, age=%s, department=%s WHERE id=%s"
    val = (name, age, department, employee_id)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee ID {employee_id} updated successfully!")

# Function to delete an employee record by ID
def delete_employee(employee_id):
    sql = "DELETE FROM employees WHERE id=%s"
    val = (employee_id,)
    cursor.execute(sql, val)
    connection.commit()
    print(f"Employee ID {employee_id} deleted successfully!")

# Menu-driven program for CRUD operations
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            create_employee(name, age, department)

        elif choice == '2':
            print("\nEmployee List:")
            read_employees()

        elif choice == '3':
            employee_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            department = input("Enter new department: ")
            update_employee(employee_id, name, age, department)

        elif choice == '4':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice! Please try again.")

# Running the menu
menu()

# Close the connection
cursor.close()
connection.close()