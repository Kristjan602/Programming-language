import main

while True:
    text = input("Main > ")
    if text == "run code":
        with open('code.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace('\n', '?')

    result, error = main.run('<stdin>', text)
    if error:
        print(error.as_string())
    elif result:
        print(result)
