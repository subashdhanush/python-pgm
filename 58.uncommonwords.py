def uncommonwords(string1,string2):
    words1=set(string1.split())
    words2=set(string2.split())
    uncommon_words_set = words1.symmetric_difference(words2)
    uncommon_words_list = list(uncommon_words_set)
    return uncommon_words_list
string1="This is the first string"
string2="This is the second string"
uncommon=uncommonwords(string1,string2)
print(uncommon)