import shelve

def write(name, text, password):
    shelfFile = shelve.open(name)
    shelfFile['password'] = password
    shelfFile['text'] = text
    shelfFile.close()

def read(name, password):
    text = None
    shelfFile = shelve.open(name)
    if password == shelfFile['password']:
        text = shelfFile['text']
    shelfFile.close()
    
    if text != None:
        return text

if __name__ == '__main__':
    text = "hello friend!"
    password = "123q"
    name = "mydata1"
    write(name, text, password)
    text2 = read(name, "123q")
    print(text2)