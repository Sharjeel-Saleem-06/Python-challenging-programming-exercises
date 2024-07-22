# Given list of names, count nmber of names starts with vowel
def list_of_names():
    count=0
    names=["aisha","iqra","sharjeel"]
    for name in names:
        if name.startswith(("a","e","i","o","u","A","E","I","O","U")):
            count+=1
    return count

print(list_of_names())

# Write a function to remove all duplicate character from a given string
def duplicate_char(str):
    for dup in str:
        if str.count(dup)>1:
            duplicate=str.replace(dup,"")
    return duplicate

print(duplicate_char("sharjeel"))

# Write a function tht takes a sentence and as a word as input and checks weather the word is present in sentence or not 
def check_word(sen):
    sentence=sen.lower()
    sentence1=sentence.split()
    
    wor=input("Enter word you want to check")
    if wor in sentence1:
        print("Word is present in sentence")
        return True
    else:
        print("Word is not present in sentence")

print(check_word("my name is sharjeel"))          

# Write a program contains two lists , and create new list which contaon same item of above two lists
def lists():
    lst1=[1,2,3,4,5,6,7,8]
    lst2=[4,5,6,11,22,33]
    lst3=[]
    for i in lst1:
        for j in lst2:
            if i==j:
                lst3.append(i)
    return lst3
print(lists())           

# Write a program to count the occurance of word in a sentence
def occurance(str):
    splitt=str.split()
    word_count={}
    for word in splitt:
        word_count[word]=word_count.get(word,0)+1
    return word_count
print(occurance("i am am sharjeel"))
