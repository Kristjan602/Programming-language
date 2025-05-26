import main

while True:
    text = input("Main > ")
    result, error = main.run('<stdin>', text)
    if error:
        print(error.as_string())
    elif result:
        print(result)
