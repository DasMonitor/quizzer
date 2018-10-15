with open("answers.txt", "r") as of:

    lines = []
    #question = str()
    seperator = ', '
    for line in of.read().split('\n'): # just for line in file if you're reading from a file
        if line:
            lines.append(line)
            #question.join(line)

            #print(question)

        else: # Empty line: stop looking
            #question = seperator.join(lines)
            #print(question)
            #lines = []
            next

    #print(seperator.join(lines))
    #print(lines) # >>> ['line 1', 'line 2', 'line 3']
    #print(lines)

    for answer in lines:
        print(answer)
