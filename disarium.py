num = int(input("Enter a number:"))
digit = [int(d) for d in str(num)]
length = len(digit)
list = []
for i in range(1,length + 1):
   list.append(digit[i-1]**i)

print(sum(list))
          