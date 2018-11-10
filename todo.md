**WEEK1**
- [ ] Find datasets for our features (abortion rates)
- [x] Plot the statistics to get an idea of the trends (difference data- plot x2-x1 instead of just x2)
- [x] Read about Chi square test for independence and look for MATLAB packages (https://www.spss-tutorials.com/chi-square-independence-test/, https://en.wikipedia.org/wiki/Chi-squared_test#Example_chi-squared_test_for_categorical_data)
- [x] Dataset sampling and cleaning (Aubhik)


**WEEK2**
- LAST WEEK
  - [x] Find datasets that we can use
  
    
- [x] plot difference in the rates and not the rates themselves
- [ ] Start writing the paper abstract and the paper introduction
- [ ] **A** - Get data from Bloomberg. Employment rate and the Dow Jones Industrial Average
- [ ] **Y** - Merge datasets of abortion rates


- I dont think it will be possible to study the effect of capital punishment as the time period is very variable. Or we can study it but in very basic terms
- We can start working on a survey in the library. Anyone who enters can be asked which factor do you think has the major effect on the decrease in crime. The survey should be anonymous and must be taken from atleast 100 students in the Stevens library.
- The plot shows that the year abortion was legalized, exactly 17-18 years later, the rate of crime dropped. This signals more causation than correlation. (STUNNING!)

- We will be changing our analysis procedure and instead of using counterfactual analysis, we will be using instrumental varibles estimation analysis (https://en.wikipedia.org/wiki/Instrumental_variables_estimation)

- To do this, we will first have to see which variables we are attempting to study have a higher correlation. And then eliminate the variables that are not strongly correlated. Example: Dow Jones and unemployment rate (CPI index/nonfarm payrolls). After this, we can use Ordinary Least Squares regression on our model to find out the causal effect of abortion


