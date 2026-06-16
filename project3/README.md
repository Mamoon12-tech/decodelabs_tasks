# Project 3 — The Data Warehouse
## DecodeLabs Cloud Computing Internship · Batch 2026

> **Mission:** Set up a managed cloud database, create an Interns table, insert dummy records, and verify data persistence using SQL queries.

---

## What I Built

A cloud database simulation using Python and SQLite3 — demonstrating the same concepts as AWS RDS MySQL. Created an `Interns` table with proper schema constraints, inserted 5 dummy records, and verified data persistence using SELECT queries.

---

## Simple Explanation

A database is just organized storage. Think of it like Excel — rows and columns. But unlike Excel it can handle millions of records, multiple users at once, and never loses data even if the server crashes.

AWS RDS is Amazon's managed database service — they handle the physical server, OS updates, and backups. You just focus on your data.

---

## Files

```
project3/
  database.py   ← Python script — creates table, inserts records, runs queries
  index.html    ← Visual page showing database output (live on GitHub Pages)
  README.md     ← This documentation
```

---

## Concepts Learned

**What is a Database?**
Organized structured storage. Like Excel but smarter — searchable, scalable, and permanent.

**SQL (Structured Query Language)**
The language used to talk to databases. Four main operations — CREATE, INSERT, SELECT, DELETE.

**AWS RDS vs DynamoDB**
RDS = relational database (rows and columns, like Excel). DynamoDB = NoSQL (flexible JSON documents). For structured intern records, RDS is the correct choice.

**PRIMARY KEY**
Every row gets a unique ID. No two rows can have the same one. Prevents duplicate records.

**NOT NULL**
This field cannot be empty. Forces complete data entry.

**UNIQUE**
No two interns can have the same email address.

**Private Subnet**
Database placed inside a private network with no direct internet route. A public database is a compromised database.

**Security Group — Port 3306**
MySQL uses port 3306. Only your IP address or EC2 bastion host can connect on this port.

---

## SQL Commands Used

```sql
-- Create table
CREATE TABLE Interns (
    InternID  INTEGER PRIMARY KEY,
    Name      VARCHAR(100) NOT NULL,
    Role      VARCHAR(100) NOT NULL,
    Email     VARCHAR(100) UNIQUE NOT NULL
);

-- Insert records
INSERT INTO Interns (InternID, Name, Role, Email)
VALUES
    (1, 'Mamoon Azam Khattak', 'Cloud Computing Intern', 'mamoonkhattak758@gmail.com'),
    (2, 'John Doe', 'Cyber Security Intern', 'jdoe@decodelabs.com'),
    (3, 'Jane Smith', 'Web Developer Intern', 'jsmith@decodelabs.com'),
    (4, 'Ali Hassan', 'Cloud Computing Intern', 'ali.hassan@decodelabs.com'),
    (5, 'Sara Khan', 'Data Science Intern', 'sara.khan@decodelabs.com');

-- Query all records
SELECT * FROM Interns;

-- Filter by role
SELECT Name, Email FROM Interns WHERE Role = 'Cloud Computing Intern';

-- Count records
SELECT COUNT(*) FROM Interns;
```

---

## How to Run the Python Script

**Option 1 — Online (no installation):**
1. Go to [replit.com](https://replit.com) or [online-python.com](https://www.online-python.com)
2. Paste the contents of `database.py`
3. Click Run
4. Screenshot the output

**Option 2 — Local (if Python installed):**
```bash
python database.py
```

---

## AWS RDS Equivalent

| Local (SQLite) | AWS Cloud (RDS) |
|---------------|-----------------|
| `sqlite3.connect('interns.db')` | `pymysql.connect(host='endpoint.rds.amazonaws.com')` |
| Local file storage | RDS instance in Private Subnet |
| No security group | Security Group — Port 3306 |
| No SSH needed | SSH Tunnel via EC2 Bastion Host |
| Free, no card | AWS Free Tier (card required) |

Same SQL commands. Same concepts. Different connection method.

---

## Live Demo

🌐 **Live Page:** https://mamoon12-tech.github.io/project3/
📁 **GitHub Repo:** https://github.com/Mamoon12-tech/decodelabs_tasks

---

## Intern Details

| Field | Value |
|-------|-------|
| Name | Mamoon Azam Khattak |
| Email | mamoonkhattak758@gmail.com |
| University | UET Peshawar · CSE · Batch 27 |
| Internship | DecodeLabs Cloud Computing — AWS/Azure |
| Project | 3 — The Data Warehouse |

---

*DecodeLabs Cloud Computing Internship · Batch 2026*
