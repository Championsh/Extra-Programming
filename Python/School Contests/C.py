def testin(k, b):
    global t
    t = []
    for i in range(k):
        sin = input().split()
        s = list(map(int, sin))
        t.append(s)
    print('t: ', t)
    variant(t, b)


def variant(t, b):
    global variants, manvar, antivariants
    variants = []
    manvar = []
    antivariants = []
    for x in t:
        if x[-1] == 1:
            manvar.append(str(x[1]))
            for i in range(x[0], x[0] + b):
                dates = [i - b + 1, i]
                m = [str(x[1]), dates]
                variants.append(m)
        if x[-1] == 0:
            m = [str(x[1]), x[0]]
            antivariants.append(m)


def meeting(m):
    global meetings
    meetings = []
    for i in range(m):
        people = []
        s = input().split()
        day = int(s[0])
        for j in range(2, len(s)):
            people.append(s[j])
        meet = [people, day]
        meetings.append(meet)


def checkvariants(variants, meetings, manvar, antivariants):
    for vari in variants:
        man = vari[0]
        for meet in meetings:
            for person in meet[0]:
                if person != man and person in manvar:
                    for var in variants:
                        if var[0] == person:
                            return 1


amount = int(input())

for amountx in range(amount):
    n, m, k, a, b = map(int, input().split())
    meeting(m)
    testin(k, b)
    print('meetings: ', meetings)
    print('variants: ', variants)
    print('antivariants: ', antivariants)
