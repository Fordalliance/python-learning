while True:
    z=int(input('0 - szyfrowanie, 1 - deszyfrowanie: '))
    if z == 0:
        #Szyfr Cezara
        text=input("Podaj słowo, które zostanie zaszyfrowane: ")
        text=text.upper()
        cipher=str()
        for c in text:
            if c.isalpha():
                code=ord(c)
                code=code+1
                if code > ord('Z'):
                    code = ord('A')
                char = chr(code)
                cipher = cipher + char
        print("Szyfr: ", cipher)
    elif z == 1:
        #Deszyfrowanie cezara

        text=input("Podaj szyfr: ")
        text=text.upper()
        cipher=str()
        for c in text:
            if c.isalpha():
                code=ord(c)
                code=code-1
                if code > ord('Z'):
                    code = ord('A')
                char = chr(code)
                cipher = cipher + char
        print("Zaszyfrowana wiadomość: ", cipher)
    else:
        print("Nieznana komenda")
