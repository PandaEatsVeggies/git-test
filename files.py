with open('config.ini', 'r') as rf:
    with open('config_copy.ini', 'w') as wf:
        for line in rf:
            wf.write(line)
