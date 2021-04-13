import random

with open("B1group.txt","r") as in1:
	list1 = [line.split("\t")[0] for line in in1.read().splitlines()]	

with open("Agroup.txt","r") as in2:
	list2 = [line.split("\t")[0] for line in in2.read().splitlines()]	
out1 = open("randomA_B1.txt","w")





list3 = []




j = 1
while j <= 10:
	
	
	nums = random.sample(list1,k=8)
	nums.extend(random.sample(list2, k = 8))
	nums.sort()
	sortednums = "_".join(str(nums))
	if sortednums in list3:
		print("id in l3")
	else:
		list3.append(sortednums)


	line = "B1_A" + " " + str(j) + " " + " ".join(nums) + "\n"

	out1.write(line)
	j += 1

out1.close()
