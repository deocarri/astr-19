def f(x):					#f is the function name and x is the input
	output = x**3 + 8		
	return output			#output is what is returned from using this function

def main():
	x=f(9)
	print(x) 				#print the result of f(9)
	if x > 27:
		print('YAY!')		#print YAY! if f(9) is bigger than 27

if __name__ == '__main__':
	main()