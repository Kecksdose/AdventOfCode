with open('data.txt', 'r') as f:
    teststr = f.read()
    open_brackets = 0
    closed_brackets = 0
    for bracket in teststr:
        if bracket is "(":
            open_brackets += 1
        elif bracket is ")":
            closed_brackets += 1
    solution = open_brackets - closed_brackets
    print "Open: {}, Closed: {}, Difference: {}".format(open_brackets,
                                                        closed_brackets,
                                                        solution)
