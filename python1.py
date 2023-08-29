Arr=["Employee ID", "Name" ,"Age" ,"Salary (PM)"]
arr1=[["161E90", "Raman", 41, 56000],
    ["161F91" ,"Himadri", 38, 67500],
    ["161F99" ,"Jaya", 51, 82100],
    ["171E20", "Tejas", 30 ,55000],
    ["171G30" ,"Ajay",45, 44000]
                                    ]

str=input("Enter Data you want to Search::")

for i in Arr:
    if str==i:
        n=Arr.index(i)
for j in range(0,5):
    print (arr1[n][j])

