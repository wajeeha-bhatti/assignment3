# main.py

import module

def main():
    name = "wajeeha"
    print(module.greet(name))

    result = module.add(5, 7)
    print(f"5 + 7 = {result}")

    number = 4
    print(f"The square of {number} is {module.square(number)}")

if __name__ == "__main__":
    main()
