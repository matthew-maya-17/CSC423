import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test4.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# GENERATE TABLES

# String variable for passing queries to cursor
query = """
    CREATE TABLE Department
    (deptName VARCHAR(100),
    chairName VARCHAR(50) NOT NULL,
    noFacultyPerDept INT,
    PRIMARY KEY (deptName),
    CONSTRAINT deptNameSyntax
        Check(deptName LIKE 'Department%'));
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Student
    (studentID VARCHAR(100),
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    initials VARCHAR(3),
    PRIMARY KEY (studentID),
    CONSTRAINT initialsLength
        Check(LENGTH(initials) > 1 ));
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Major
    (majorID VARCHAR(15),
    majorName VARCHAR(100) NOT NULL,
    majorCode VARCHAR(3) UNIQUE NOT NULL,
    deptName VARCHAR(100) NOT NULL,
    CONSTRAINT majorCodeRequiredLength
        Check(LENGTH(majorCode) = 3 ),
    PRIMARY KEY (majorID),
    Foreign Key (deptName) references Department ON DELETE CASCADE);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Event
    (eventID VARCHAR(12),
    eventName VARCHAR(100) NOT NULL,
    startDate DATE,
    endDate DATE,
    CONSTRAINT endDateGreater
        Check(endDate > startDate),
    CONSTRAINT startDateGreater
        Check(startDate > '11-DEC-2021'),
    PRIMARY KEY (eventID));
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Academics
    (studentID VARCHAR(100),
    majorID VARCHAR(15),
    PRIMARY KEY (studentID, majorID),
    Foreign Key (studentID) references Student ON DELETE CASCADE,
    Foreign Key (majorID) references Major ON DELETE CASCADE);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Attendance
    (studentID VARCHAR(100),
    eventID VARCHAR(12),
    PRIMARY KEY(studentID, eventID),
    FOREIGN KEY(studentID) REFERENCES Student ON DELETE CASCADE,
    FOREIGN KEY(eventID) REFERENCES Event ON DELETE CASCADE);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Hostee
    (deptName VARCHAR(100),
    eventID VARCHAR(12),
    PRIMARY KEY(deptName, eventID),
    FOREIGN KEY(deptName) REFERENCES Department ON DELETE CASCADE,
    FOREIGN KEY(eventID) REFERENCES Event ON DELETE CASCADE);
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

#INSERT INTO TABLES

# -------------------------- STUDENT INSERTS ------------------------------
query = """
    INSERT INTO Student
    Values('S001', 'Matthew', 'Maya', 'MM');
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    Values('S002', 'Nicky', 'Sosnivka', 'NS');
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    Values('S003', 'Gabe', 'Simmons', 'GB');
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    Values('S004', 'Paul', 'Rhoades', 'PR');
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    Values('S005', 'Juan', 'Arango', 'JA');
    """
cursor.execute(query)

# -------------------------- DEPARTMENT INSERTS ----------------------------
query = """
    INSERT INTO Department
    VALUES ('Department of Arts & Science', 'Steve Jobs', 92);
    """
cursor.execute(query)

query = """
   INSERT INTO Department
   VALUES ('Department of Communications', 'Oprah Winfrey', 103);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ('Department of Engineering', 'Elon Musk', 34);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ('Department of Marine & Atmospheric Science', 'Steve Irwin', 57);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ('Department of Business', 'Jordan Belfort', 65);
    """
cursor.execute(query)

# ----------------------------- EVENT INSERTS --------------------------------
query = """
    INSERT INTO Event
    VALUES('E001', 'Homecoming', '2022-11-01', '2022-11-07');
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES('E002', 'Walk to Defeat ALS', '2022-05-23', '2022-05-24');
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES('E003', 'Welcome Week Festival', '2022-08-26', '2022-08-27');
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES('E004', 'Black Lives Matter', '2022-02-01', '2022-03-01');
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES('E005', 'Walk to End Poverty', '2022-01-15', '2022-01-16');
    """
cursor.execute(query)

# ----------------------------- MAJOR INSERTS ---------------------------------
query = """
    INSERT INTO Major
    VALUES('M002', 'Computer Science', 'CSC', 'Department of Engineering');
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES('M003', 'Biology', 'BIO', 'Department of Arts & Science');
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES('M015', 'Marine Biology', 'MAR', 'Department of Marine & Atmospheric Science');
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES('M023', 'Journalism', 'JOU', 'Department of Communications');
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES('M031', 'Marketing', 'MKT', 'Department of Business');
    """
cursor.execute(query)

# ----------------------------- ACADEMICS INSERTS ---------------------------------
query = """
    INSERT INTO Academics
    VALUES ('S004', 'M002');
    """
cursor.execute(query)

query = """
    INSERT INTO Academics
    VALUES ('S002','M003');
    """
cursor.execute(query)

query = """
  INSERT INTO Academics
  VALUES ('S003', 'M015');
    """
cursor.execute(query)

query = """
    INSERT INTO Academics
    VALUES ('S001', 'M023');
    """
cursor.execute(query)

query = """
    INSERT INTO Academics
    VALUES ('S005', 'M031');
    """
cursor.execute(query)

# ----------------------------- ATTENDANCE INSERTS ---------------------------------
query = """
    INSERT INTO Attendance
    VALUES ('S002', 'E002');
    """
cursor.execute(query)

query = """
    INSERT INTO Attendance
    VALUES ('S004', 'E004');
    """
cursor.execute(query)

query = """
    INSERT INTO Attendance
    VALUES ('S001', 'E001');
    """
cursor.execute(query)

query = """
    INSERT INTO Attendance
    VALUES ('S003', 'E003');
    """
cursor.execute(query)

query = """
    INSERT INTO Attendance
    VALUES ('S005', 'E001');
    """
cursor.execute(query)

# ----------------------------- HOSTEE INSERTS ---------------------------------
query = """
    INSERT INTO Hostee
    VALUES ('Department of Business', 'E001');
    """
cursor.execute(query)

query = """
    INSERT INTO Hostee
    VALUES ('Department of Communications', 'E004');
    """
cursor.execute(query)

query = """
    INSERT INTO Hostee
    VALUES ('Department of Communications', 'E002');
    """
cursor.execute(query)

query = """
    INSERT INTO Hostee
    VALUES ('Department of Marine & Atmospheric Science', 'E004');
    """
cursor.execute(query)

query = """
    INSERT INTO Hostee
    VALUES ('Department of Marine & Atmospheric Science', 'E005');
    """
cursor.execute(query)

# ----------------------------------- TABLES ---------------------------------
# Select data
query = """
    SELECT *
    FROM Student
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

query = """
    SELECT *
    FROM Department
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

query = """
    SELECT *
    FROM Event
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

query = """
    SELECT *
    FROM Major
    """
cursor.execute(query)

query = """
    SELECT *
    FROM Academics
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

query = """
    SELECT *
    FROM Attendance
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

query = """
    SELECT *
    FROM Hostee
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

# -------------------------- QUERIES ---------------------------------------
query = """
    SELECT s.studentID, s.firstName, s.lastName
    FROM Major m, Academics a, Student s
    WHERE a.majorID = m.majorID AND a.studentID = s.studentID AND m.majorCode LIKE 'BIO';
    """
cursor.execute(query)
# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()



query = """
    SELECT h.deptName
    FROM Hostee h, Event e
    WHERE h.eventID = e.eventID AND e.eventName LIKE 'Walk to Defeat ALS' AND e.startDate > '2020-12-31' AND e.endDate < '2022-01-01';
    """
cursor.execute(query)
# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()



query = """
    SELECT majorName, majorCode, majorID
    FROM Department d, Major m
    WHERE d.deptName = m.deptName AND d.deptName lIKE '%Arts & Science%';
    """
cursor.execute(query)
# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()



query = """
    SELECT d.noFacultyPerDept
    FROM Department d, Major m
    WHERE d.deptName = m.deptName AND d.deptName LIKE 'Department of Engineering';
    """
cursor.execute(query)
# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()



query = """
    SELECT s.studentID, s.firstName, s.lastName
    FROM Student s, Attendance a, Event e
    WHERE a.studentID = s.studentID AND a.eventID = e.eventID AND e.eventName LIKE 'Black Lives Matter';
    """
cursor.execute(query)
# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()
# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
