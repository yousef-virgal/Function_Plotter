# Function_Plotter

Function_Plotter is an application that lets users plot a polynomial function starting from minimum
value and ending at a maximum value specfied by the user
 

### Notes

* The maxmium possible range to draw the function is from -9999 to 9999
* The expected regular expression for the function is as follows 
   1. multiplyOrDivision = * | / 
   2. addOrSubtract = + | -
   3. higherExp = lowerExp | lowerExp addOrSubtract higherExp  
   4. lowerExp = node | node multiplyOrDivision lowerExp
   5. node = number | number X (^number)? | X (^number)? 
   6. number = integer | float  

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the requirements.txt file 
> pip install -r requirements.txt
4. Run the app.py file 

## Examples

Plotting X<sup>2</sup> from -10 to 10

![X^2 plot](/screenshots//X%5E2_plot.png)

Plotting X<sup>2</sup> + 10X <sup>5</sup> from -100 to 0

![X^5 plot](/screenshots/x%5E5_plot.png)

Entering minimum value greater than the maximum value

![error_1](/screenshots/error1.png)

Entering an invalid token
![error_2](/screenshots/error2.png)

Entering a wrong expression 
![error_3](/screenshots/error3.png)



