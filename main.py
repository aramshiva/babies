import mysql.connector, os
from dotenv import load_dotenv

def create_database(db_config):
    conn = mysql.connector.connect(**db_config)
    c = conn.cursor()
    
    c.execute(f"USE {os.getenv('DATABASE_NAM')};")

    Create table (if dosent exist already )
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {names} (
            name VARCHAR(255),
            sex CHAR(1),
            amount INT,
            year INT
        )
    ''')
    conn.commit()
    return conn

def process_files(folder_path, db_conn, total_rows):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    processed_rows = 0
    
    for file in files:
        year = int(file[3:7])  # Extract year from filename "yobYYYY.txt"
        with open(os.path.join(folder_path, file), 'r') as f:
            for line in f:
                name, sex, amount = line.strip().split(',')
                insert_data(db_conn, name, sex, int(amount), year)
                processed_rows += 1
                print_progress(processed_rows, total_rows, name, year, sex)

def insert_data(conn, name, sex, amount, year):
    c = conn.cursor()
    c.execute('''
        INSERT INTO names (name, sex, amount, year) 
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE amount=amount
    ''', (name, sex, amount, year))
    conn.commit()

def print_progress(current, total, name, year, sex):
    percentage = (current / total) * 100
    if sex == "F": sex = "Female"
    elif sex == "M": sex = "Male"
    else: sex = "Unknown"
    print(f"Processed {current}/{total} rows ({percentage:.2f}%) ({sex} {name} for {year})")

def main():
    db_config = {
        'user': os.getenv('DATABASE_USR'),
        'password': os.getenv('DATABASE_PWD'),
        'host': os.getenv('DATABASE_HST'),
        'raise_on_warnings': True
    }
    
    folder_path = os.getenv('FOLDER_PATH')  # Path to the folder containing the files
    total_rows = 2117219  # you can calculate this automatically if you really wanted
    # as of 2023, the total rows is 2,117,219. This is the total number of rows in all files combined.
    
    try:
        conn = create_database(db_config)
    except Exception as e:
        print("Error creating database:", e)
        return
    
    # Process each file and insert data into the database
    try:
        process_files(folder_path, conn, total_rows)
    except Exception as e:
        print("Error processing files:", e)
    
    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
