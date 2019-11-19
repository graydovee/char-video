import os

def out(path, text):
    if ensure(path):
        with open(path, "w") as file:
            file.write(text)
    else:
        print("error: invalid path!")

def ensure(path):
    path.replace("\\", "/")
    l = path.rfind("/")
    if l >= 0:
        if not os.path.exists(path[:l]):
            os.makedirs(path[:l])
        else:
            if os.path.isfile(path[:l]):
                print("error: is not a dir!")
                return False

    return True
