from adminChecker import adminChecker
from connection import  Connection


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    adminCheck = adminChecker(username, password)
    adminResult = adminCheck.adminChecker()
    print(adminResult)
    if adminResult:
        while True:
            print("Hello admin!!")
            print("----------menu----------")
            print("[A] Show all books")
            print("[B] Add book")
            print("[C] Remove book")
            print("[D] Update book")
            print("[E] Exit")
            print("\n")
            choice = input("Enter your choice: ")
            match choice:
                case "A":
                    pass
                    break
                case "B":
                    pass
                    break
                case "C":
                    pass
                    break
                case "D":
                    pass
                    break
                case "E":
                    print("Programme terminated!!")
                    break
                case __:
                    print("Invalid choice")
                    break










if __name__ == "__main__":
    main()





