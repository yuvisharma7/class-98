def countwords(): 
    f=input("enter the file name:")
    numberOfWords=0 
    file= open(f,'r')
    for i in file: 
        words=i.split ()
        numberOfWords= numberOfWords + len(words)
    print("number of words",numberOfWords)
countwords()