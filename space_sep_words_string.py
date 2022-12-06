#Input from user
st = input("Enter a string \n")
#Splitting using space as a delimiter
words = st.split()
#Printing
print("First two characters of all words are: ", end="")
for word in words:
    print(word[:2], end=" ")