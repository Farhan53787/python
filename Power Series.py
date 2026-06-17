num = int(input("Enter the number of terms: "))
for term in range(1,num + 1):
    print("{}^{}={}".format(term, term, term**term))