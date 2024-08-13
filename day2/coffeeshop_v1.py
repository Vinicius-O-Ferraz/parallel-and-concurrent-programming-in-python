import time

def brew_coffee()->str:
    print("Start brew_coffee()")
    time.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

def toast_bagel():
    print("Start toast_bagel()")
    time.sleep(2)
    print("End toast_bagel()")
    return "Bagel toasted"

def main():
    start_time = time.time()

    result_coffee = brew_coffee()
    result_bagel = toast_bagel()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(result_coffee)
    print(result_bagel)
    print(f" Your breakfast is ready in {elapsed_time:2f}")

if __name__ == '__main__':
    main()