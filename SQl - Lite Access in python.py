import sqlite3

con = sqlite3.connect('users.db')


def InsertData(name, age, city):
    qry = "insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry, (name, age, city))
    con.commit()
    print("User details added")


def UpdateData(name, age, city, id):
    qry = "update users set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry, (name, age, city, id))
    con.commit()
    print("User details Updated")


def DeleteData(id):
    qry = "delete from users where id=?;"
    con.execute(qry, (id))
    con.commit()
    print("User details Deleted")


def SelectData():
    qry = "select * from users"
    result = con.execute(qry)
    for i in result:
        print(i)


print("""
--------------
1.Insert
2.Update
3.Delete
4.select
---------------
""")

ch = 1
while ch == 1:
    c = int(input("Enter a Choice : "))
    # insert data:
    if (c == 1):
        print("Insert a Record")
        name = input("Enter a Name : ")
        age = input("Enter a age : ")
        city = input("Enter a city : ")
        InsertData(name, age, city)

    # Update data:
    elif (c == 2):
        print("Update a record")
        id = input("Enter a id : ")
        name = input("Enter a Name : ")
        age = input("Enter a age : ")
        city = input("Enter a city : ")
        UpdateData(name, age, city, id)

    # delete data:
    elif (c == 3):
        print("Delete a record")
        id = input("Enter a ID : ")
        DeleteData(id)

    # select data:
    elif (c == 4):
        print("Select a record")
        SelectData()
    else:
        print("Invalid Record")
    ch = int(input("Enter 1 to Continue : "))
print("Thank you...!")
