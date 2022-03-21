task_list = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(type(task_list))

#prink KES
print(task_list[2][2]["currency"])

#print 560
print(task_list[2][1])

#length
print(len(task_list))

#reverse 987
rev = str(task_list[-2])[::-1]
task_list[-2] = rev
print(task_list)

#change john to jan
k = list((task_list[-1]))
k[1] = "Jane"
t = tuple(k)
task_list[-1] = t
print(task_list)

#add amount

#task_list.append(["Amount":90])
#print(task_list)
