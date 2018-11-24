PROC IMPORT OUT= WORK.CRIME_RATES
            DATAFILE= "C:\Users\Aubhik\Desktop\CausalInference\datasets\regression.csv" 
            DBMS=CSV REPLACE;
     GETNAMES=YES;
     DATAROW=2; 
RUN;
proc standard data=work.crime_rates MEAN=0 STD=1 OUT=ZCRIME_RATES;
	var crime_rate abortion dowjones incarceration;
RUN;


proc reg data=zcrime_rates;
	model crime_rate=abortion dowjones incarceration;
quit;
