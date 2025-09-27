import sys

class Main():
    def __init__(self):
        retval = self.welcome()
        while True:
            try:
                rv_temp = retval()
            except:
                continue

            retval = rv_temp

    def welcome(self):
        print("\nWelcome to Docus Pocus")
        print(
            " 1. Create document\n" \
            " 2. Check test coverage\n" \
            " q. Quit"
        )
        match input("Please select an option [1-n]\n > "):
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
            " 1. Statement of Work\n" \
            " 2. Requirements & design specification\n" \
            " 3. Test plan\n" \
            " 4. Test report\n" \
            " 8. Review form\n" \
            " 9. Instructions & procedures\n" \
            " q. Back"
        )
        match input(f"{20*'='}\nPlease select an option [1-n]\n > "):
            case "1":
                print("Very nice")
                return self.create_document
            case "q":
                return self.welcome
            case _:
                print("Try again")
                return self.create_document

    def exit(self):
        sys.exit()
    

if __name__=="__main__":
    Main()
