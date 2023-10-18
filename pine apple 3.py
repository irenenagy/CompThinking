def LexicographicSort(sampleData):
    Data = sampleData.split()
    Data.sort()
    for a in Data:
        print(a)


sampleData = "pine apple"
print("String before using Lexicographical Order: ", sampleData)
print("String after using Lexicographical Order: ")

LexicographicSort(sampleData)