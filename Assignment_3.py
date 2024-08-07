        #MATHS_OPARETOR THAT TAKES TWO NUMS
#Definiton of numbers
def Math_operations(num1, num2):
    '''
    math_operations function takes two integers parameters
    uses lambda fuction to calculate sum, product, quotient and difference of the numbers
    '''
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

def main():
    result = Math_operations(48, 12)
    print("Sum: ", result["sum"])
    print("Product: ", result["product"])
    print("Quotient: ", result["quotient"])
    print("Difference: ", result["difference"])

if __name__ == '__main__':
    main()
