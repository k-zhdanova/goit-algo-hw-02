from palindrome_app.main import main as run_palindrome_app
from queue_app.main import main as run_queue_app


def main():
    try:
        print(
            "Which app do you want to run? \n (1) Queue \n (2) Palindrome \n (q) Quit \n"
        )
        action = input()

        if action == "1":
            run_queue_app()

        elif action == "2":
            run_palindrome_app()

        elif action == "q":
            print("\nGood bye!")
            return
        else:
            print("\033[91mI don't understand that command\033[0m")

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


if __name__ == "__main__":
    main()
