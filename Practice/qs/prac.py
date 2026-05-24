import pandas as pd
import mysql.connector

# Load Excel file
df_excel = pd.read_excel(r"D:\PROGRAM\PYTHON\Practice\detail_student.xlsx") # Ensure 'id' and 'year' columns exist

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",           # Update if different
    user="root",       # 🔁 Replace with your MySQL username
    password="Arsuljawed@123",   # 🔁 Replace with your MySQL password
    database="SQL_PATH"    # 🔁 Replace with your MySQL DB name
)
cursor = conn.cursor(dictionary=True)

# For storing matched results
matched_rows = []

# Loop through each row in Excel and fetch matching data from MySQL
for index, row in df_excel.iterrows():
    student_id = int(row['student_id'])  # 🔁 Ensure 'student_id' matches your Excel column name
    year = int(row['year'])
    
    query = "SELECT * FROM STUDENT_DATA WHERE STUDENT_ID = %s AND year = %s"  # 🔁 Replace 'student_table' with your actual table name
    cursor.execute(query, (student_id, year))
    result = cursor.fetchall()
    
    if result:
        matched_rows.extend(result)

# Convert matched result into a DataFrame
df_matched = pd.DataFrame(matched_rows)

if 'PHONE' in df_matched.columns:
    df_matched['PHONE'] = df_matched['PHONE'].astype(str)

# Save the matched data to a new Excel file
if not df_matched.empty:
    df_matched.to_excel("matched_data.xlsx", index=False)
    print("✅ Matching data saved to 'matched_data.xlsx'")
else:
    print("❌ No matching records found in the database.")

# Cleanup
cursor.close()
conn.close()
