import sqlite3

from EMPLOYEEEEESSSS import  Employee
conn= sqlite3.connect('my.db')

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES (?,?,?)", (emp.first, emp.last, emp.pay))


def get_emps_by_name(lastname):
    with conn:
        c.execute("SELECT * FROM employee WHERE last=?", (lastname,))
        return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employee WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


c= conn.cursor()
# c.execute("""CREATE TABLE employee(
#     first text,
#     last text,
#     pay integer
#
# )""")
emp1= Employee('john','sid',20000)
emp2= Employee('sam','sid',20000)



insert_emp(emp1)
insert_emp(emp2)
epm= get_emps_by_name('sid')

print epm

update_pay(emp1,20)
remove_emp(emp2)
epm= get_emps_by_name('sid')

print epm

conn.close()

# print emp2

# c.execute("INSERT INTO employee VALUES (?,?,?)",(emp1.first,emp1.last,emp1.pay))
# conn.commit()
# c.execute("INSERT INTO employee VALUES (?,?,?)",(emp2.first,emp2.last,emp2.pay))
# conn.commit()

# print c.execute("SELECT * FROM employee WHERE last=?",('dolly',))

# print (c.fetchall())
# conn.commit()

conn.close()