import vard

print("Welcome to VardScript 1.2")
while True:
    try:
        text = input('VardScript > ')
        if text.strip() == "": continue
        result, error = vard.run('<stdin>', text)
        if error:
            print(error.as_string())
    except KeyboardInterrupt:
        print("Use halt() to terminate shell")