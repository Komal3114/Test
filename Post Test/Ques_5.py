"""
Q5. Create a File Reader System: (5 Marks) 
• Ask user to enter a filename 
• Try to open and read the file 
• If file not found → print 'File does not exist!' 
• If file is empty → print 'File is empty!' 
• If success → print total number of lines in file 
• Add finally block → print 'Operation complete!'
"""

try:
    filename = input("Enter filename : ")

    file = open(filename,"r")
    content = file.readlines()

    if len(content) == 0:
        print("File is Empty!")
    
    else:
        print("Total number of lines in files:", len(content))


    file.close()

except FileNotFoundError:
    print("File does not exist")

finally:
    print("Operation Complete!")   