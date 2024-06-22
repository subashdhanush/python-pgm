result=[]
def findwords(word_list,k):
    for i in word_list:
        if len(i) > k:
            result.append(i)

word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k=5
longwords=findwords(word_list,k)
print(result)