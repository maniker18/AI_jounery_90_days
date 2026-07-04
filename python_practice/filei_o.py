# try:
#     file = open(r"C:\Users\LENOVO\Documents\chatgpt api.txt",'r')
#     for line in file.readlines():
#       print(line)

#     print(file.read())
#     file.close()
# except FileNotFoundError:
#    print("File not found. Please check the file path and try again.")



# file2 = open("dxd","w")
# file2.write("hello ")

# # 
# with open(r"C:\Users\LENOVO\Desktop\AI_jounery_90_days\readme\day_05_py.md","r") as f:
#     # print(f.readlines())

#     # for line in f:
#     #     print(line,end='')
    
#     size_to_read =50 
#     fline = f.read(size_to_read)
#     while len(fline) > 0:
#         print(fline,end='')
#         fline = f.read(size_to_read)

with open(r"C:\Users\LENOVO\Desktop\AI_jounery_90_days\readme\day_05_py.md","r") as f:
    with open("file.txt",'w') as wf:
        for line in f:
            wf.write(line)




# with open("file.txt",'r') as f:
#     print(f.read())




