import sqlite3
# Connect to SQLite database
connection = sqlite3.connect("grpby.db")

# Create cursor object
cursor = connection.cursor()

# Drop existing tables and create new ones
cursor.executescript("""
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Director;
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS DVD;

CREATE TABLE Actor(
    Actor_ID INTEGER,
    Actor_name TEXT,
    Gender TEXT,
    debut_year INTEGER
);

CREATE TABLE Director(
    Director_ID INTEGER,
    Director_name TEXT,
    no_of_movies INTEGER
);

CREATE TABLE Movie(
    Movie_name TEXT,
    release_year INTEGER,
    genre TEXT,
    lead_1 INTEGER,
    lead_2 INTEGER,
    director_id INTEGER,
    box_collection INTEGER
);

CREATE TABLE DVD(
    DVD_id INTEGER,
    Movie_name TEXT,
    sale INTEGER
);
""")

# Insert records into Actor table
cursor.executescript("""
INSERT INTO Actor VALUES(1,'Aamir Khan','Male',1988);
INSERT INTO Actor VALUES(2,'Shahrukh Khan','Male',1992);
INSERT INTO Actor VALUES(3,'Kareena Kapoor','Female',2000);
INSERT INTO Actor VALUES(4,'Kajol','Female',1992);
INSERT INTO Actor VALUES(5,'Anushka Sharma','Female',2008);
INSERT INTO Actor VALUES(6,'Ranbir Kapoor','Male',2007);
INSERT INTO Actor VALUES(7,'Alia Bhatt','Female',2012);
INSERT INTO Actor VALUES(8,'Ranveer Singh','Male',2010);
INSERT INTO Actor VALUES(9,'Deepika Padukone','Female',2006);
INSERT INTO Actor VALUES(10,'Shahid Kapoor','Male',2003);
INSERT INTO Actor VALUES(11,'Katrina Kaif','Female',2003);
INSERT INTO Actor VALUES(12,'Varun Dhawan','Male',2012);
""")

# Insert records into Director table
cursor.executescript("""
INSERT INTO Director VALUES(1,'Rajkumar Hirani',10);
INSERT INTO Director VALUES(2,'Sanjay Leela Bhansali',8);
INSERT INTO Director VALUES(3,'Aditya Chopra',6);
INSERT INTO Director VALUES(4,'Zoya Akhtar',3);
INSERT INTO Director VALUES(5,'Imtiaz Ali',5);
INSERT INTO Director VALUES(6,'Ayan Mukerji',4);
INSERT INTO Director VALUES(7,'Santosh Sivan',9);
INSERT INTO Director VALUES(8,'Farah Khan',4);
""")

# Insert records into Movie table
cursor.executescript("""
INSERT INTO Movie VALUES('3 Idiots',2009,'Comedy',1,3,1,989600000);
INSERT INTO Movie VALUES('PK',2014,'Satire',1,5,1,789600000);
INSERT INTO Movie VALUES('Bajirao Mastani',2015,'Historic',8,9,2,68960000);
INSERT INTO Movie VALUES('Rab ne bana di jodi',2008,'Romance',2,5,3,48960000);
INSERT INTO Movie VALUES('Gully Boy',2019,'Musical Drama',8,7,4,28950000);
INSERT INTO Movie VALUES('Jab We Met',2007,'Romance',10,3,5,18980000);
INSERT INTO Movie VALUES('Padmavat',2018,'Historic',8,9,2,38460000);
INSERT INTO Movie VALUES('Yeh Jawani Hai Deewani',2013,'Romance',6,9,6,581600000);
INSERT INTO Movie VALUES('Ashoka',2001,'Historic',2,3,7,8796000);
INSERT INTO Movie VALUES('Happy New Year',2014,'Comedy',2,9,8,68960000);
""")

# Insert records into DVD table
cursor.executescript("""
INSERT INTO DVD VALUES(1,'3 Idiots',8890);
INSERT INTO DVD VALUES(2,'PK',8790);
INSERT INTO DVD VALUES(3,'Bajirao Mastani',6810);
INSERT INTO DVD VALUES(4,'Rab ne bana di jodi',7920);
INSERT INTO DVD VALUES(5,'Gully Boy',870);
INSERT INTO DVD VALUES(6,'Jab We Met',4792);
INSERT INTO DVD VALUES(7,'Padmavat',590);
INSERT INTO DVD VALUES(8,'Yeh Jawani Hai Deewani',2890);
INSERT INTO DVD VALUES(9,'Ashoka',730);
INSERT INTO DVD VALUES(10,'Happy New Year',1690);
""")

# Commit changes
connection.commit()

# Display Actor table
print("\n========== ACTOR TABLE ==========")
cursor.execute("SELECT * FROM Actor")
for row in cursor.fetchall():
    print(row)

# Display Director table
print("\n========== DIRECTOR TABLE ==========")
cursor.execute("SELECT * FROM Director")
for row in cursor.fetchall():
    print(row)

# Display Movie table
print("\n========== MOVIE TABLE ==========")
cursor.execute("SELECT * FROM Movie")
for row in cursor.fetchall():
    print(row)

# Display DVD table
print("\n========== DVD TABLE ==========")
cursor.execute("SELECT * FROM DVD")
for row in cursor.fetchall():
    print(row)

# Close connection
connection.close()

print("\nDatabase 'grpby.db' created successfully.")