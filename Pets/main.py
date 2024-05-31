import mysql.connector as mc
import subprocess

# Connect to the database
# Adjust lines 6-10 to suit your needs
conn = mc.connect(
    host='localhost',
    user='root',
    password='Bl@ckcl0ver'
)
c = conn.cursor()

def create_database():
    """Create the database"""
    # Optional: drop the database if it exists
    c.execute('DROP DATABASE IF EXISTS menagerie')
    c.execute('CREATE DATABASE menagerie')
    c.execute('USE menagerie')

def create_table():
    """Create table in the database"""
    c.execute('CREATE TABLE pet ('
              'name VARCHAR(20), '
              'owner VARCHAR(20), '
              'species VARCHAR(20), '
              'sex CHAR(1), '
              'birth DATE, '
              'death DATE)')
    c.execute('DESCRIBE pet')
    for table in c:
        print(table)

def add_data_to_table():
    """Add data to the table and display it"""
    c.execute("USE menagerie")
    c.execute("INSERT INTO pet VALUES('Fluffy','Harold','cat','f','1993-02-04',NULL)")
    c.execute("INSERT INTO pet VALUES('Claws','Gwen','cat','m','1994-03-17',NULL)")
    c.execute("INSERT INTO pet VALUES('Buffy','Harold','dog','f','1989-05-13',NULL)")
    c.execute("INSERT INTO pet VALUES('Fang','Benny','dog','m','1990-08-27',NULL)")
    c.execute("INSERT INTO pet VALUES('Bowser','Diane','dog','m','1979-08-31','1995-07-29')")
    c.execute("INSERT INTO pet VALUES('Chirpy','Gwen','bird','f','1998-09-11',NULL)")
    c.execute("INSERT INTO pet VALUES('Whistler','Gwen','bird',NULL,'1997-12-09',NULL)")
    c.execute("INSERT INTO pet VALUES('Slim','Benny','snake','m','1996-04-29',NULL)")
    c.execute("INSERT INTO pet VALUES('Puffball','Diane','hamster','f','1999-03-30',NULL)")

    # Commit the transaction
    conn.commit()

    fetch_data_query = 'SELECT * FROM pet'
    c.execute(fetch_data_query)

    # Fetch all rows from the executed query
    rows = c.fetchall()

    # Get column names from cursor description
    columns = [desc[0] for desc in c.description]

    # Display the column names
    print(f"{' | '.join(columns)}")
    print("-" * 50)

    # Display each row
    for row in rows:
        print(f"{' | '.join(map(str, row))}")

def female_dogs():
    c.execute("USE menagerie")
    fetch_data_query = 'SELECT * FROM pet Where species = "dog" and sex = "f"'
    c.execute(fetch_data_query)

    # Fetch all rows from the executed query
    rows = c.fetchall()

    columns = [desc[0] for desc in c.description]

    # Display the column names
    print(f"{' | '.join(columns)}")
    print("-" * 50)

    # Display each row
    for row in rows:
        print(f"{' | '.join(map(str, row))}")

def birth_name():
    c.execute("USE menagerie")
    fetch_data_query = 'SELECT name, birth FROM pet'
    c.execute(fetch_data_query)

    # Fetch all rows from the executed query
    rows = c.fetchall()

    columns = [desc[0] for desc in c.description]

    # Display the column names
    print(f"{' | '.join(columns)}")
    print("-" * 50)

    # Display each row
    for row in rows:
        print(f"{' | '.join(map(str, row))}")

def count():
    c.execute("USE menagerie")
    fetch_data_query = 'SELECT owner, COUNT(*) FROM pet GROUP BY owner'
    c.execute(fetch_data_query)

    # Fetch all rows from the executed query
    rows = c.fetchall()

    columns = [desc[0] for desc in c.description]

    # Display the column names
    print(f"{' | '.join(columns)}")
    print("-" * 50)

    # Display each row
    for row in rows:
        print(f"{' | '.join(map(str, row))}")


def birth_month():
    c.execute("USE menagerie")
    fetch_data_query = 'SELECT name, birth,MONTH(birth) FROM pet'
    c.execute(fetch_data_query)

    # Fetch all rows from the executed query
    rows = c.fetchall()

    columns = [desc[0] for desc in c.description]

    # Display the column names
    print(f"{' | '.join(columns)}")
    print("-" * 50)

    # Display each row
    for row in rows:
        print(f"{' | '.join(map(str, row))}")
def output():
    output_file = "new_database_dump.sql"
    subprocess.run([
        mysqldump_path,
        "-h", host,
        "-u", user,
        f"--password={password}",
        ,
        "-r", output_file
    ])

if __name__ == '__main__':
    create_database()
    create_table()
    add_data_to_table()
    female_dogs()
    birth_name()
    count()
    birth_month()
    output
    # Close the cursor and connection
    c.close()
    conn.close()
