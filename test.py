#!/usr/bin/env python
# vim: set fileencoding=utf-8 :




distribution = { }

shengmu_table = [
                    'a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'sh', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'zh',

                ]




for shengmu in shengmu_table :
    distribution[shengmu] = [ ]

def str2int(s):
    return int( s.encode("hex"), 16)

def pickout_delimiter( numbers) :

    length = len(numbers)
    ret = [ ]

    head = numbers[0]
    tail = numbers[-1]

    base = 0

    #ret.append(head)

    for i in range(1, length-1) :

        if numbers[i] - numbers[i-1] >1 :

            continous_length = (i-1) - base + 1
            #ret.append( (numbers[base], continous_length) )
            ret.append( (continous_length, numbers[base] ) )

            base = i

    ret.append( (1,tail)  )

    # sort by continous length
    ret.sort()

    return ret


def get_shengmu( accent):

    assert len(accent) >= 2

    shengmu = accent[:2] if accent[1] == 'h' else accent[0]
    return shengmu



lines = open("utf8.txt").readlines()

for line in lines :

    line = line[:-1] if line[-1] == '\n' else line
    line = unicode( line, "utf8")

    unichar, accent = line.split('=')
    accent = accent.lower()

    shengmu = get_shengmu(accent)

    try :
        gbkchar = unichar.encode("GB18030")
        distribution[shengmu].append ( str2int(gbkchar) )
    except:
        pass

shengmus = distribution.keys()
shengmus.sort()

for shengmu in shengmus:

    distribution[shengmu].sort()
    chars = distribution[shengmu]

    if chars and shengmu == 'zh' :
        delimiters = pickout_delimiter (chars)
        print "%s: contain %d chars" % (shengmu, len(chars) )
        print "[%s]" % chars

        result = ""

        delimiters = delimiters[-5:]

        for delimiter in delimiters:
            result += "(%d,0x%x) " % (delimiter[0], delimiter[1])

        print result

