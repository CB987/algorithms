#rite a program that prints the words to the song "99 bottles of beer", counting down until 1 bottle is left. You'll want functions that print a single line ("XX bottles of beer on the wall, XX bottles of beer. Take one down, pass it around, XY bottles of beer on the wall")

bottles = 99

while bottles > 0:
    if bottles == 2:
        print("%d bottles of beer on the wall, \n %d bottles of beer. \nTake one down, pass it around, \n %d bottle of beer on the wall" % (bottles, bottles, (bottles-1)))
        print ()
    elif bottles == 1:
        print("%d bottles left. \n Next beer run on you! \n Don't drink and drive!" % (bottles-1))
        print()
    else:
        print("%d bottles of beer on the wall, \n %d bottles of beer. \nTake one down, pass it around, \n %d bottles of beer on the wall" % (bottles, bottles, (bottles-1)))
        print()
    bottles -= 1

