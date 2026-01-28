import zipfile

# Open the .apkg file
with zipfile.ZipFile("50_key_history_dates.apkg", "r") as zip_ref:
    # Extract all contents to a temporary directory
    zip_ref.extractall("temp_extracted")

# Now you can process the extracted files as needed
import os
import sqlite3
import json
import shutil

# Path to the extracted SQLite database
db_path = os.path.join("temp_extracted", "collection.anki2")
# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# Query to get all notes
cursor.execute("SELECT id, flds FROM notes")
notes = cursor.fetchall()
# Process each note
for note_id, flds in notes:
    fields = flds.split("\x1f")  # Anki uses \x1f as field separator
    if len(fields) >= 2:
        question = fields[0]
        answer = fields[1]
        print(f"Question: {question}\nAnswer: {answer}\n")
# Close the database connection
conn.close()
# Clean up the temporary extracted files
shutil.rmtree("temp_extracted")
