#f = open("../TEI/fiction_and_essays/Варианты к После бала 34.xml")
f = open("../TEI/fiction_and_essays/[О суде] 29.xml")
f.close()
#content = f.read()
content = f.readlines()
#print(content)
for p in content:
    if "Михайл" in p:
        print(p)

