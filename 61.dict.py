my_dict={
    'a':10,
    'b':20,
    'c':30,
    'd':10,
    'e':20,
    'f':30
}
unival=set()
for i in my_dict.values():
    unival.add(i)

univallist=list(unival)
print(univallist)