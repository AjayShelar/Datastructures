def LinearSearch(Myitem, Mylist):
	found = False
	position = 0

	while position < len(Mylist) and not found:
		if Mylist[position] == Myitem:
			found = True
		position = position + 1
	return found

if __name__=="__main__":
	shopping = ["apples", "bananas", "oranges", "mangoes"]
	item = input("enter item  ")
	isitfound = LinearSearch(item, shopping)
	if isitfound:
		print(item," is in list")
	else:
		print(item, " not in list")

