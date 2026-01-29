import apkgExtraction


def main():
    questions_answers = apkgExtraction.ankiExtract("testdata.apkg")  # returns a dict
    print(questions_answers)


if __name__ == "__main__":
    main()
