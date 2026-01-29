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


def extract_anki_notes(apkg_path):
    # Open the .apkg file
    with zipfile.ZipFile(apkg_path, "r") as zip_ref:
        # Extract all contents to a temporary directory
        zip_ref.extractall("temp_extracted")

    # Path to the extracted SQLite database
    db_path = os.path.join("temp_extracted", "collection.anki2")
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Query to get all notes
    cursor.execute("SELECT id, flds FROM notes")
    notes = cursor.fetchall()
    # Process each note

    questions_answers = {}

    for _, flds in notes:
        fields = flds.split("\x1f")  # Anki uses \x1f as field separator
        if len(fields) >= 2:
            questions_answers[fields[0]] = fields[1]

    # Close the database connection
    conn.close()
    # Clean up the temporary extracted files
    shutil.rmtree("temp_extracted")
    return questions_answers


def main():
    questions_answers = extract_anki_notes("50_key_history_dates.apkg")
    print(questions_answers)


if __name__ == "__main__":
    main()
