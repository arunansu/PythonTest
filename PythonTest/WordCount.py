doc = "offer is secret click secret link secret sports link play sports today went play sports secret sports event sports is today sport costs money"
worddict = {}
for word in doc.split():
    if word in worddict:
        worddict[word] += 1
    else:
        worddict[word] = 1

print worddict.keys()