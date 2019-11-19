from PIL import Image
import Out


def createText(path, arg1=-1, arg2=-1):
    img = Image.open(path).convert('L')

    width, height = img.size
    if arg1 != -1 and arg2 == -1:

        if arg2 == -1:
            width = int(width * float(arg1))
            height = int(height * float(arg1))
        
        else:
            width = int(width)
            height = int(height)

    width = width * 2
    img = img.resize((width, height))

    asc = '@&%#*+=-. '
    text = ''
    for row in range(height):
        for col in range(width):
            gray = img.getpixel((col, row))
            text += asc[int(gray / 255 * 9)]
        text += '\n'
    return text
