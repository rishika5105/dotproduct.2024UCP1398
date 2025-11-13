#input two vectors with space separated components
v1= input("Enter first vector: ").split()
v2= input("Enter second vector: ").split()

#convert each element from string to float
v1= [float(x) for x in v1] 
v2= [float(x) for x in v2] 

#dot product 
dot_product =0
for i in range(len(v1)):
	dot_product += v1[i] * v2[i]
	
#result
print("Dot Product: ",dot_product)
=======
#input two vectors as space separated numbers
v1 = input("Enter first vector : ").split()
v2 = input("Enter second vector : ").split()

#Convert each element from string to float
v1 = [float(x) for x in v1]
v2 = [float(x) for x in v2]

#dot product 
dot_product = 0
for i in range(len(v1)):
    dot_product += v1[i] * v2[i]

print("Dot product:", dot_product)

print("hello from both branches")

