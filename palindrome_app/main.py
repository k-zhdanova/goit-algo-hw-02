from collections import deque


def is_palindrome(input):
    str = input.lower().replace(" ", "")

    str_deque = deque(str)

    while len(str_deque) > 1:
        if str_deque.popleft() != str_deque.pop():
            return False

    return True


def main():
    str = input("Enter a string: ")

    if is_palindrome(str):
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")


if __name__ == "__main__":
    main()
