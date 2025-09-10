names =set()
while True:
    name = input ("new name: ")
    if len (name) == 0:
        print (names)
        break
    if name in names:
        print( "Existing name: ")
    else:
        print ("New name: ")
    names. add (name)