import sys
import json
import csv
import shutil
from pathlib import Path

SELECT_OPTION_STRING = f"{20*'='}\nPlease select an option [1-n]\n > "


class Main:
    def __init__(self):
        retval = self.welcome()
        while True:
            try:
                rv_temp = retval()
            except:
                continue

            retval = rv_temp

    def welcome(self):
        print(f"\nWelcome to Docus Pocus\n{20*'='}")
        print(" 1. Create document\n" " 2. Check test coverage\n" " q. Quit")
        match input(SELECT_OPTION_STRING):
            case "1":
                return self.create_document
            case "q":
                return self.exit
            case _:
                print("Try again")
                return self.welcome

    def create_document(self):
        print(f"\nCreate document\n{20*'='}")
        print(
            " 1. Statement of Work\n"
            " 2. Requirements & design specification\n"
            " 3. Test plan\n"
            " 4. Test report\n"
            " 8. Review form\n"
            " 9. Instructions & procedures\n"
            " q. Back"
        )
        match input(SELECT_OPTION_STRING):
            case "1":
                return self.create_sow
            case "3":
                return self.create_test_plan
            case "q":
                return self.welcome
            case _:
                print("Try again")
                return self.create_document

    def create_sow(self):
        print(f"\nCreate Statement of Work\n{20*'='}")
        src_file = Path("./templates/statement_of_work.md")
        docs_dir = Path.cwd() / Path("docs")

        projects = [x for x in docs_dir.iterdir() if x.is_dir()]
        [print(f" {i}. {p.name}") for i, p in enumerate(projects)]
        proj = input(SELECT_OPTION_STRING)

        try:
            dst_file = projects[int(proj)] / Path(f"sow_{projects[int(proj)].name}.md")
        except:
            print("Try again")
            return self.create_sow

        shutil.copy(src_file, dst_file)
        return self.welcome

    def create_test_plan(self):
        # Select the controlling document
        docs = list(Path("docs").glob("*/sow_*"))
        print(f"\nControlling documents containing requirements to test\n{20*'='}")
        [print(f" {i}. {doc.name}") for i, doc in enumerate(docs)]
        i = int(input(SELECT_OPTION_STRING))
        requirements_doc = docs[i]

        # Search for the requirements table in the controlling document
        with open(requirements_doc) as f:
            requirements_table_lines = []
            while True:
                line = f.readline()
                if "[Table: Requirements]" in line:
                    break

            while True:
                line = f.readline()
                if "|" not in line:
                    break

                requirements_table_lines.append(line)

        [print(line) for line in requirements_table_lines]
        return self.welcome

    def exit(self):
        sys.exit()


if __name__ == "__main__":
    Main()
