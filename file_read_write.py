
with open('test1.txt', 'r') as rf:
    with open('test2.txt', 'a') as wf:
        read_contents = rf.read()
        while len(read_contents) > 0:
            wf.write(read_contents)
            read_contents = rf.read()
                        
