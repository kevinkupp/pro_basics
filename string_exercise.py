#Sõne-tüüpi muutujate deklareerimine
first_name = "James"
last_name = "Bond"
print(first_name + " " + last_name)
#Sõnede kujundamine - names
first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {full_name}."
print(self_description_sentence)
#Sõnede kujundamine - cake string
cake = "vahukoormarjadtäidispõhi"
print("vahukoor\nmarjad\ntäidis\npõhi")
#Sõnede tükeldamine
original_string = "Programming is fun!"

backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string.split()[0][::-1]

print(backwards)
print(every_other)
print(first_word_reversed)
