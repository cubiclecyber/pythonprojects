from operator import index


fullclass = ["Becca", "Solo", "Robinson", "Vashti", "Jay", "Stephen"]
print(len(fullclass))

onlineclass = [fullclass[3],fullclass[-1]]
print(onlineclass)

physicalclass = [fullclass[1], fullclass[2]]
print(physicalclass)

hybridclass = [fullclass[0], fullclass[4]]
print(hybridclass)

hybridclass.append(fullclass[1])
print(hybridclass)

modifiedphysical = physicalclass.remove(fullclass[1])
print(physicalclass)