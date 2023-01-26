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

## Examples


