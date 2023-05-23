#!/usr/bin/python3
index = 'isrveawhobpnutfg'
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in abc:
    if index[ord(i) & 0xf] in 'giants':
        print("{} : {}".format(index[ord(i) & 0xf], i))
