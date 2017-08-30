from PIL import Image

# http://stackoverflow.com/questions/10657383/stitching-photos-together

# MIN = 1
# MAX = 12

X_MIN = 1
X_MAX = 20
Y_MIN = 1
Y_MAX = 16

def padTwoDigits(number):
    if number < 10:
        return "0" + str(number)
    return str(number)

def getFilename(y, x):
    return padTwoDigits(y) + "_" + padTwoDigits(x) + ".png"

def main():

    tiles = {}
    totalWidth = 0
    totalHeight = 0

    for y in range(1, Y_MAX+1):
        tiles[y] = {}
        for x in range(1, X_MAX+1):
            fileName = getFilename(y, x)
            tile = Image.open(fileName)
            tiles[y][x] = tile

    print tiles

    for i in range(1, Y_MAX+1):
        (_, height) = tiles[i][1].size
        totalHeight += height


    for j in range(1, X_MAX+1):
        (width, _) = tiles[1][j].size
        totalWidth += width

    print totalWidth
    print totalHeight

    (baseWidth, baseHeight) = tiles[1][1].size
    # totalWidth = X_MAX * baseWidth
    # totalHeight = Y_MAX * baseHeight

    result = Image.new('RGB', (totalWidth, totalHeight))
    for y in range(1, Y_MAX+1):
        for x in range(1, X_MAX+1):
            tile = tiles[y][x]
            h = (y-1) * baseWidth
            w = (x-1) * baseHeight
            result.paste(im=tile, box=(w,h))

    result.save("stitch.png")


main()
