# with open ("tempfile.txt","r") as f:
#     # read_file = f.read() #cursor ends at  last value so it wil not read from start
#     size = 25
#     line =f.read(size)
#     # line  = f.readlines()
#     # print(line)
#     while len(line)>0:
#         print(line,end = "---")
#         line =f.read(size)
#     # for li in f:
#     #     print(li,end = "")
        
#     # print(read_file)

with open("tempfile.txt","r") as rf:
    with open("temp_copy_ile.txt","w") as wf:
        for line in rf:
            wf.write(line)

with open("temp_copy_ile.txt","w") as wf:
    wf.seek(0)
    for i in range(10):
        wf.write(f" {str(i)} this is {str (i)} line \n")
    
    
    