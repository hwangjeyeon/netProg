word = input("Your Word: ")

finds = word.find("a")
print(word[:finds+1])
print(word[finds+1:])