

from ntpath import join
from posixpath import split


trainees = ["John", [2, ["Mary","J"]],38, 40.0]
#1. Display 2 using index, from the list.

z =trainees[1][0]
print(z)
#2. Output J using index, from the list.

j=trainees[1][1][1]
print(j)
#3. Using a method add 56 at the end of the list.

trainees.append(56)
print(trainees)
#4. Using a method add the name Mike between Mary and J

trainees[1][1].insert(1, "Mike")
print(trainees)

#5. Change the value of 38 to 48
trainees[2] = 48
print(trainees)

#6. Remove John and ["Mary",”Mike”, "J"] from the list.
del trainees[0], trainees[0][1]
print(trainees)


#7. Using a function, determine the length of the list
trainees[0] = trainees[0][0]
s = sum(trainees)
print(s)