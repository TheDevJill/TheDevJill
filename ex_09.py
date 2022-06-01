han=open('intro.txt')
count=dict()

for line in han:
    word=line.split()
    count[word]=count.get(line,0)+1
print(count)
