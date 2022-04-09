import random
import time

min = 1
max = 6

tavidan = "ki"

while tavidan == "ki":
    print("\n-> KAMATELI MIGORAVS SHORRRSSSS...\n")
    time.sleep(1)
    print("-> KAMATELI MOGORDA SHENTAN....\n")
    time.sleep(1)
    print("== PIRVELI KAMATELI: " + str(random.randint(min, max)) + "\n")
    time.sleep(1)
    print("== MEORE KAMATELI: " + str(random.randint(min, max)) + "\n")
    time.sleep(1)

    print("-> DAVAI NARDIC VITAMASHOT\n")
    time.sleep(1)
    print("-> miutite 'ki' tu kidev ginda tamashi\n")
    time.sleep(1)
    print("-> daachire Enter-s tu agar ginda tamashi\n")
    time.sleep(1)

    tavidan = input("-> GAVAGORO TAVIDAN KAMATELI JO?(ki/ara) ")
