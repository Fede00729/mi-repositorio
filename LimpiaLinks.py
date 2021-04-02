fname = input("Enter file name: ")
if len(fname) < 1 : fname = "‪D:\zz.python\LinksParaBajar.txt"

fh = open(fname)

for line in fh:
	pos = line.find('http:')
	link = line[pos:]
	link = link.strip()
	print(link)


#for line in fh:
#    line = line.strip()
#    if line.startswith('From '):
#        count = count + 1
#        line = line.split()
#        print(line[1])
input()
