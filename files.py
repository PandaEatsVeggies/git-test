with open('L7126.jpg', 'rb') as rf:
    with open('L7126_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            print(len(chunk))
            wf.write(chunk)
            chunk = rf.read(chunk_size)
