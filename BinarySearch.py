def BinarySearch(Myitem, Mylist):
	found = False
	bottom = 0
	top = len(Mylist) - 1
	
	while bottom <= top and not found:
		middle = (top + bottom) // 2
		if Mylist[middle] == Myitem:
			found = True
		elif Mylist[middle] < Myitem:
			bottom = middle + 1
		else:
			top = middle - 1
	return found

if __name__ == '__main__':

	LIST = [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14]
	item = int(input("enter item"))


	isitfound = BinarySearch(item, LIST)
	
	if isitfound:
		print("its found")
	else:
		print("not found")