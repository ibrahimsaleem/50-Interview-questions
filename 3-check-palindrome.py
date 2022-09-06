#palindrome
#a word, phrase, or sequence that reads the same backwards as forwards, 
# e.g. madam or civic.

#so we make program to check if a given string a palindrome

s = str(input("Enter word ot check palindrome :")) #taking input string
s = list(s)             #converting all string Characters into a list
s2 = list(reversed(s))  #reverseing the list and making new list s2

if(s==s2):              #condtion if s and s2 is same it will be palindrome
    s= "".join(s)
    print(s," is palindrome")
else:
    s= "".join(s)
    print(s," is not-palindrome")


######### Method - 2 ##########

# function to check palindrome
def checkPalindrome(str):
   
    # Run loop from 0 to len/2
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
           
    # If the above loop doesn't
    #return then it is palindrome
    return True
 
 
# Driver code
str = "112233445566778899000000998877665544332211"
if(checkPalindrome(str) == True):
    print("it is a palindrome")
else:
    print("It is not a palindrome")
