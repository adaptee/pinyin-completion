#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


shengmu_table = {
            #'a' : [ ],
            #'b' : [ ],
            #'c' : [ ],
            #'d' : [ ],
            #'e' : [ ],
            #'f' : [ ],
            #'g' : [ ],
            #'h' : [ ],
            #'i' : [ ],
            #'j' : [ ],
            #'k' : [ ],
            #'l' : [ ],
            #'m' : [ ],
            #'n' : [ ],
            #'o' : [ ],
            #'p' : [ ],
            #'q' : [ ],
            #'r' : [ ],
            #'s' : [ ],
            #'t' : [ ],
            #'u' : [ ],
            #'v' : [ ],
            #'w' : [ ],
            #'x' : [ ],
            #'y' : [ ],
            #'z' : [ ],
}


def get_shengmu( accent):
    return accent[0]

if __name__ == "__main__":

    lines = open("utf8.txt").readlines()

    for line in lines :

        line = line[:-1] if line[-1] == '\n' else line
        line = unicode( line, "utf-8")

        unichar, accent = line.split('=')
        accent = accent.lower()

        shengmu = get_shengmu(accent)

        try :
            shengmu_table[unichar].append(shengmu)
        except KeyError:
            shengmu_table[unichar] = [shengmu,]

    print  "# vim: set fileencoding=utf-8 :"
    print  ""
    print  "table = {"

    for key in shengmu_table.keys():
        print "u'%s' : %s ," % (key.encode("utf-8"),  shengmu_table[key] )

    print "}"
    #print shengmu_table

