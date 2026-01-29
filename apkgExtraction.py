import zipfile
import os
import sqlite3
import shutil


def ankiExtract(apkg_path):

    with zipfile.ZipFile(apkg_path, "r") as zip_ref:  # open the .apkg file
        # Extract all contents to a temporary directory
        zip_ref.extractall("temp_extracted")

    # Path to the extracted SQLite database
    db_path = os.path.join("temp_extracted", "collection.anki2")
    conn = sqlite3.connect(db_path)  # connect to the SQL database
    cursor = conn.cursor()
    # Query to get all notes
    cursor.execute("SELECT id, flds FROM notes")
    notes = cursor.fetchall()

    questions_answers = {}

    for _, flds in notes:
        fields = flds.split("\x1f")  # Anki uses \x1f as field separator
        questions_answers[fields[0]] = fields[1]  # add questions and answers to dict

    conn.close()  # close the database connection
    shutil.rmtree("temp_extracted")  # clean temp files

    return questions_answers
