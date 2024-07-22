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

# Write a function
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

