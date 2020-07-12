# Statistical_thinking
### COVARIANCE ###
Covariance is a statistical tool that is used to determine the relationship between the movement of two asset prices.
When two stocks tend to move together, they are seen as having a positive covariance; when they move inversely, the covariance is negative.
FOR EXAMPLE: I want to buy some products and I don't know their are good or not so I found that data from google and see X and Y company growth rate during this and last year
Then I calculate X and Y company Mean
Then to see goodness find the diffrerence between each value and mean price.
Multiply the result of X and Y Difference
using that final number and find the COVARIANCE.
If the answer is POSITIVE so I notice that company X and Y are good to buy any product, And If the answer is negative Products are not good to buy.
### BINOMIAL DISTRIBUTION ##########
The binomial distribution model allows us to compute the probability of observing a specified number of "successes" when the process is repeated a specific number of times (e.g., in a set of patients) and the outcome for a given patient is either a success or a failure.
IN Another Example: If I want to see in JUNK_FOOD_VS_HEALTHY_FOOD Project What type of JUNK_FOOD prefered by GENDER. IN THIS CASE MY DEPENDENT VARIABLE IS GENDER OR IS CATEGORICAL
VARIABLE AND OUR INDEPENDENT VARIABLE IS TYPE OF JUNK_FOOD. AND WE GOT SOME DATA THAT HOW MUCH LIKE JUNK_FOOD GENDER ARE.

###  POISSON DISTRIBUTION  ####

In statistics, a Poisson distribution is a statistical distribution that shows how many times an event is likely to occur within a specified period of time. It is used for independent events which occur at a constant rate within a given interval of time.
The Poisson distribution is a discrete function, meaning that the event can only be measured as occurring or not as occurring, meaning the variable can only be measured in whole numbers either 0 or 1.
### POLYNOMIAL REGRESSION ###
IF THE DATA IS NOT FIT ON THE LINE THAN WE USE POLYNOMIAL REGRESSION
### LINEAR REGRESSION : Y = B0 + B1X1
### MULTIPLE LINEAR REGRESSION : Y = B0 + B1X1 + B2X2 + ... + BnXn
### POLYNOMIAL REGRESSION : Y = B0 + B1X1 + B2(X1)2 + ... + Bn(X1)n
In polynomial regression, you try to find the coefficients of a polynomial of a specific degree that best fits the data. Linear regression is the special case where . Linear regression is linear in the parameters, not the covariates. You can make any transformations you want of them and still have a linear model.
Polynomial provides the best approximation of the relationship between the dependent and independent variable.
A Broad range of function can be fit under it.
Polynomial basically fits a wide range of curvature.
### R Square | COEFFICIENT OF DETERMINATION  ####
R-squared (R2) is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. ... It may also be known as the coefficient of determination.
It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything. The relationship is measured with a value called the r-squared. The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

### JUNK_FOOD_VS_HEALTHY_FOOD #######################
### IN THIS PROJECT WE WANT TO IDENTIFY THAT WHAT TYPE OF AGE GROUP PREFERE JUNK FOOD OR HEALTHY FOOD AND WHAT TYPE OF GENDER AND MARRIED OR UNMARRIED PEOPLE EAT JUNK FOOD OR HEALTHY FOOD IN WEEKLY AND SPECIFICLY WHAT THEY PREFARE. IF THEY CHECK THE NUTRIENT FACT LABEL IN JUNK FOOD OR NOT.
IN THIS PROJECT I GO WITH SOME DATA. I COLLECT THE DATA WITH GOOGLE QUESTIONNAIRES. QUESTIONS IS ALL ABOUT HOW OFTEN DO YOU EAT JUNK FOOD IN A WEEK, HOW OFTEN DO YOU EAT HEALTHY 
FOOD IN A WEEK, HOW DO YOU CONSIDER HEALTHY FOOD IS (LOW FAT FOOD, LOW CALORIES,FOOD THAT MAKE YOU ENERGETIC AND FIT AT THE SAME TIME,ALL OF THE ABOVE),WHAT KIND OF JUNK_FOOD DO YOU EAT(BURGERS AND FRIES,PIZZA,HARDIES,ALL OF THE ABOVE),WHAY DO YOU EAT HEALTHY FOOD,AT WHAT TIME YOU EAT JUNK FOOD OR HEALTHY FOOD,DO YOU CHEAK THE NUTRIENT FACT LABEL IN THE 
JUNK FOOD,DO YOU CHECK THE JUNK FOOD QUALITY.
### DATA CLEANING AND UNDERSTAND THE DATA
In this data I see that information and find null values, use drop mathod to drop some columns and use dummy variable for Gender and Marital Status
In this data I use describe mathod TO FIND OUT THE SKWENESS AND I SAW MOST OF THE COLUMNS ARE NEAR TO MEDIAN AND THAT IS GOOD.
### VISUALIZATION
### SEABORN
### MATPLOTLIB
### BOXPLOT
WITH THE GRAPH WE CAN SAY THAT MARRIED PEOPLE CHOSSING TO EAT JUNK_FOOD BECAUSE OF THERE VARIETY OF MENU.
FEMALE ARE CHOSSING TO EAT JUNK_FOOD BECAUSE THEY ENJOY THE TEAST, SOME CHOSSING THE JUNK_FOOD BECAUSE THEY HAVE LIMITED TIME AND SOME OF CHOOSE TO EAT JUNK_FOOD TO SPEND TIME WITH FRIENDS AND FAMILY.
UNMARRIED PEOPLE PREFARE TO CHECK THE NUTRIENT FACT LABEL IN THE JUNK_FOOD.
25% FEMALE ARE CHECK NUTRIENT FACT LABEL,25% FEMALE DON'T KNOW ABOUT IT,25% FEMALE ARE CHECK SOMETIMES AND FEW ARE DON'T CHECK.
UNMARRIED PEOPLE EAT JUNK_FOOD TO ENJOY THE TEST,75% VARIETY OF MENU AND FEW ARE TO SPEND TIME WITH THERE FAMILY AND FRIENDS.
THERE IS AN MALE/FEMALE SERIES WHO EAT PIZZA AND ANY KIND OF JUNK FOOD.
25% MARRIED PEOPLE PREFARE ONLY SANDWITCHES.
UNMARRIED FEMALE DO CHECK THE NUTRIENT FACT LABEL IN JUNK FOOD.
