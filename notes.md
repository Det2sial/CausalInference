ABORTION AND CRIME RATES IN NYC

TODO
====

  1. Write abstract and introduction
  2. Start analysis
  
-------------------------------------------------------------------------------

Tehcniques we can use
=====================

  1. Reduced form equation
  2. Counterfactual analysis by comparing data with cities where legalized abortion was not present before 1973 (Roe vs Wade)
  3. Instrumental Variables analysis for isolating the effect of the surge in crime rates due to crack-cocaine abuse
  4. Stratified Propensity score analysis for comparing 2 different cities (think of Chicago, Sydney etc.)
  5. Difference-in-difference analysis
  6. t-ratio to check the validity of our regressions
  7. SAS software for our regressions. Extremely easy and accurate
  
-------------------------------------------------------------------------------

Things we have to consider
==========================

  * Confounding effect of crime rise due to crack-cocaine abuse during the 1980s and ending in the early 1990s
  * Abortion data may be by state of residence or by state of occurence (medical tourism)
  * Does the rise of abortion rates truly mean that there were less unwanted children? NO! Other inventions like birth contraception and non-stationarity of data (number  of births per capita also fell between 1970-1975)

-------------------------------------------------------------------------------

Criticize yourself
==================

* The data we have may not be accurate
* The sampling size is not enough
* The effect of legalizing abortion may have taken some time to take effect
* Like most randomised trials, there is an effect of contamination as many people took part in medical tourism especially between 1970-1973 for abortion

-------------------------------------------------------------------------------

Working strategies
==================
  * Read the paper "abortion and crime" (Joyce et al.)
  * Start learning the techniques mentioned above mainly
	*  Reduced form analysis
	*  Instrumental variables analysis
  * Grab datasets mentioned in the paper above

-------------------------------------------------------------------------------

Why is crime not related to abortion rates?
===========================================
  * **counterfactual analysis**
	* The fertility rate is the same in states where abortion was legal before 1973, but the abortion rate is almost double. In this case, crime in the legal states should have gone down but that is not the case
	* Second, teens born in legal states actually commit more crimes than those in non-legal states ( even though abortion was legal in legal states)
	* 

-------------------------------------------------------------------------------


DATA SETS
=========
  * FBI's uniform crime reports - 1985 to 1997 crime data
  * National center for Health Statistics Multiple Causes of Death files for the years 1985-1997 (homicide rates => crime rates proxy)
  * FBI homicide reports - contain information of the perpetrator as well
  * US census bureau - population by state and race for teens aged 15 to 19
  * National Center for health statistics - fertility rates form 1961 to 1985
    * Using this data, we can relate the crime rates based on age and race to the lagged race-specific fertility rates
	
-------------------------------------------------------------------------------

What should we do?
==================
  * Did crime rates in states with abortion reduce more than those without legal abortion?
  * First compare rate of increase/decrease in arrest rates for
	* 18 year olds in legal states during 1971-1973
	* 18 year olds born between 1971-1973 in non-legal states
  * Next, compare arrest/crime rates of 18 year olds born in 1969 and 1971(treatment group, were exposed to legalized abortion in 1971 but not in 1969) and those of 19 year olds born in 1968 and 1970 (control group, not exposed to abortion) 
  * After this, the changes in rates in the legal states can be compared with the same in the non-legal states (18year olds | legal vs 18year olds | non-legal)



Diff1 = arrest rates of 18 year olds born in 1969 - arrest/crime rates of 18 year olds born in 1980

Diff2 = arrest/crime rates of 19 year olds born in 1968 - arrest/crime rates in 19 year olds born in 1980 

Diff3 = arrest rates of 18 year olds born in 1971 - arrest rates of 18 year olds born in 19..

Diff4 = arrest rates of 18 year olds born in 1971 - arrest rates of 19 year olds born in 19..


Once we have these values we have removed all the confounding effects due to the cohort effect and the period and age effects. This will serve as our counterfactual and will be used in our final analysis



Secondly, we can use the linear/logistic regression model to find the average values of the BETA values for all the intercepts.

Ln(crime_rate) = alpha + BETA1 * (abortion rate)......

Read the papers again to see how they have used the regression models in their studies.


Average Causal effect = Diff1 - Diff2

Week 3
======

  * Find number of police per state per year
  * Get dow jones average per year
  * 
