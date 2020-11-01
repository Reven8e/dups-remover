FILE = input('(i) Please enter file name (must be txt file!): ')

lines_seen = set()  # holds lines already seen

outfile = open('no_dups.txt', "w")
for line in open(f'{FILE}.txt', "r"):
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
