%% Multinomial Logistic Regression

% read csv file and create table
% header = {'Year','Abortion','DowJones','Incarceration','Crime_Rate'};

data = csvread("E:\code\project\dataset\regression.csv",1,0);
year = data(:,1);
abortion = data(:,2);
dowjones = data(:,3);
incarceration = data(:,4);
crime_rate = data(:,5);
T = table(year,abortion,dowjones,incarceration,crime_rate);

% multinomial logistic regression
X = [abortion,dowjones,incarceration];
Y = crime_rate;

% Y = categorical(crime_rate);
% % B: coefficicent estimates
% % dev: deviance of the fit
% % stats: model statistics
% [B,dev,stats] = mnrfit(X,Y,'Model','ordinal','link','logit'); 

Model=fitlm(X,Y,'linear');