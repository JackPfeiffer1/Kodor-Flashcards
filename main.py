import apkgExtraction


def main():
    questions_answers = apkgExtraction.extract_anki_notes("50_key_history_dates.apkg")
    print(questions_answers)


if __name__ == "__main__":
    main()
