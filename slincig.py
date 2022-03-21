

from itertools import count


name = "Robinson Koech"

#String indexing
part1  = name[-1]
print(part1)
#string slicing
#first part takes the index(from 0)
#second part takes the count(from 1)

sentence_one = "The Dog Breed is German Shepherd"
part1 = sentence_one[8:23]
print(part1)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
part2 = sentence_two[16:30]
print(part2)

# “The lazy dog; ran so fast; it hit the wall.”
whole_sent = "The lazy dog; ran so fast; it hit the wall."
first_sent = whole_sent[0:13]
print(first_sent)
print(first_sent.count(""))

second_sent = whole_sent[14:26]
print(second_sent)
print(second_sent.count(""))

last_sent = whole_sent[27:43]
print(last_sent)
print(last_sent.count(""))
print(whole_sent.count(""))

x = whole_sent.split(";")
print (x)
print(len(x))