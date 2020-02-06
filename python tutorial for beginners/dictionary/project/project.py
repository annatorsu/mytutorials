phone_number=input("please type your phone number")
number_in_words={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
    
        
}
output=""
for ch in phone_number:
        output+=number_in_words.get(ch, "!")+""
        
print(output)
