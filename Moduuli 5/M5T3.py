onalkuluku = True

luku = int(input("Anna luku:"))

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        onalkuluku = False
        break

if (onalkuluku == True):
    print ("lukusi on alkuluku")
else:
    print ("lukusi ei ole alkuluku.")
