        #MATHS_OPARETOR THAT TAKES TWO NUMS
#Definiton of numbers
def Math_operations(num1, num2):
    """"
lambda arguments : expression
lambda functions can take any number of arguments
    """
#Lambda functions 
    mySum = lambda num1, num2 : num1 + num2

    myProduct = lambda num1, num2 : num1 * num2

    myQuotient = lambda num1, num2 : num1 / num2

    myDifference = lambda num1, num2 : num1 - num2
    #Return function
    return{
    "sum" : mySum(num1, num2),
    "product" : myProduct(num1, num2),
    "quotient" : myQuotient(num1, num2),
    "difference" : myDifference(num1, num2)
}
#Doctstring for math_operations
result = Math_operations(32, 8)

print("Sum: ", result["sum"])
print("Product: ", result["product"])
print("Quotient: ", result["quotient"])
print("Difference: ", result["difference"])
