input = input("Enter a sentence or any phrases: ")
def palindrome(input):
    input = input.replace(" ", "").lower()
    return input == input[::-1]
print(palindrome(input))