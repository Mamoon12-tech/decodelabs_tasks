import sqlite3
from datetime import datetime

# ============================================================
# DecodeLabs Cloud Computing Internship - Batch 2026
# Project 3: The Data Warehouse
# Intern: Mamoon Azam Khattak
# ============================================================

print("=" * 55)
print("  DecodeLabs — Project 3: The Data Warehouse")
print("  Simulating AWS RDS MySQL using SQLite3")
print("=" * 55)
print()

# STEP 1: Connect to database (creates file if not exists)
# In AWS RDS this would be: pymysql.connect(host='endpoint.rds.amazonaws.com')
conn = sqlite3.connect('decodelabs_interns.db')
cursor = conn.cursor()
print("[✓] Database connection established")
print("    Cloud equivalent: AWS RDS MySQL instance provisioned")
print()

# STEP 2: Create the Interns table with proper schema
# PRIMARY KEY - every row has a unique ID, no duplicates
# NOT NULL    - these fields cannot be empty
# UNIQUE      - no two interns can have same email
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Interns (
        InternID   INTEGER PRIMARY KEY,
        Name       VARCHAR(100) NOT NULL,
        Role       VARCHAR(100) NOT NULL,
        Email      VARCHAR(100) UNIQUE NOT NULL
    )
''')
conn.commit()
print("[✓] Table 'Interns' created successfully")
print("    Schema: InternID | Name | Role | Email")
print("    Constraints: PRIMARY KEY, NOT NULL, UNIQUE enforced")
print()

# STEP 3: Insert dummy records (INSERT INTO statement)
# This is DML - Data Manipulation Language
interns_data = [
    (1, 'Mamoon Azam Khattak', 'Cloud Computing Intern',   'mamoonkhattak758@gmail.com'),
    (2, 'John Doe',            'Cyber Security Intern',    'jdoe@decodelabs.com'),
    (3, 'Jane Smith',          'Web Developer Intern',     'jsmith@decodelabs.com'),
    (4, 'Ali Hassan',          'Cloud Computing Intern',   'ali.hassan@decodelabs.com'),
    (5, 'Sara Khan',           'Data Science Intern',      'sara.khan@decodelabs.com'),
]

# Clear existing records first to avoid duplicates on re-run
cursor.execute('DELETE FROM Interns')

cursor.executemany('''
    INSERT INTO Interns (InternID, Name, Role, Email)
    VALUES (?, ?, ?, ?)
''', interns_data)
conn.commit()
print(f"[✓] {len(interns_data)} dummy records inserted successfully")
print("    SQL used: INSERT INTO Interns (InternID, Name, Role, Email) VALUES (...)")
print()

# STEP 4: SELECT query to verify data persistence
# This proves the data is stored permanently
print("[✓] Executing: SELECT * FROM Interns;")
print()
cursor.execute('SELECT * FROM Interns')
rows = cursor.fetchall()

# Display results in a formatted table
print("-" * 75)
print(f"{'InternID':<10} {'Name':<25} {'Role':<25} {'Email':<20}")
print("-" * 75)
for row in rows:
    print(f"{row[0]:<10} {row[1]:<25} {row[2]:<25} {row[3]:<20}")
print("-" * 75)
print()
print(f"[✓] {len(rows)} records retrieved — Data persistence verified!")
print()

# STEP 5: Additional queries to demonstrate SQL operations
print("[✓] Bonus Query — Filter by Role:")
cursor.execute("SELECT Name, Email FROM Interns WHERE Role = 'Cloud Computing Intern'")
cloud_interns = cursor.fetchall()
for intern in cloud_interns:
    print(f"    → {intern[0]} | {intern[1]}")
print()

print("[✓] Bonus Query — Count total interns:")
cursor.execute("SELECT COUNT(*) FROM Interns")
count = cursor.fetchone()[0]
print(f"    → Total interns in database: {count}")
print()

# Close connection
conn.close()
print("=" * 55)
print("  Mission Status: DATA WAREHOUSE OPERATIONAL")
print(f"  Executed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 55)
