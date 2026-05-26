"""4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data"""
n=input("Enter string=")
seen=[]
w=n.split()
for i in range(0, len(w)):
    count=0
    for j in range(0, i+1):
        if w[i]==w[j]:
            count=count+1
    if count==1:
        print(w[i],end=" ") 
    else:
        print(w[i]+"("+str(count-1)+")",end=" ")       