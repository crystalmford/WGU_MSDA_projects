#Detection Code

#install packages
library(tidyverse)
library(visdat)
library(readr)

#import dataset
churn_raw_data<-read_csv("churn_raw_data.csv")
view(churn_raw_data)

#Look for duplicates
sum(duplicated(churn_raw_data))

#Rename dataset so I will quit typing wrong name 
churn<-churn_raw_data

#Look for NAs in dataset
colSums(is.na(churn))

#Visualize the missing data in dataset
vis_miss(churn)

#Determine  datatype for each column
str(churn)

#Verify distributions before and after imputations
hist(churn$Children)
hist(churn$Tenure)
hist(churn$Income)
hist(churn$Bandwidth_GB_Year)

#Impute median for missing values in Children, Tenure, Income, Bandwidth_GB_Year due to bi-modal distribution
churn$Children[is.na(churn$Children)]<-median(churn$Children, na.rm=TRUE)
churn$Tenure[is.na(churn$Tenure)]<-median(churn$Tenure, na.rm=TRUE)
churn$Income[is.na(churn$Income)]<-median(churn$Income, na.rm=TRUE)
churn$Bandwidth_GB_Year[is.na(churn$Bandwidth_GB_Year)]<-median(churn$Bandwidth_GB_Year, na.rm=TRUE)

#Impute mean for missing values in Age due to normal distribution
churn$Age[is.na(churn$Age)]<-mean(churn$Age, na.rm=TRUE)

#Impute mode for missing values in Techie, TechSupport and Phone due to categorical variables
churn$Techie[is.na(churn$Techie)]<-names(which.max(table(churn$Techie)))
churn$Phone[is.na(churn$Phone)]<-names(which.max(table(churn$Phone)))
churn$TechSupport[is.na(churn$TechSupport)]<-names(which.max(table(churn$TechSupport)))

#Verify distributions before and after imputations
hist(churn$Children)
hist(churn$Tenure)
hist(churn$Income)
hist(churn$Bandwidth_GB_Year)
hist(churn$Age)

#Determine the outliers for all quantitative variables
churn$Children_z<-scale(x=churn$Children)
churn$Age_z<-scale(x=churn$Age)
churn$Income_z<-scale(x=churn$Income)
churn$Outage_z<-scale(x=churn$Outage_sec_perweek)
churn$Contacts_z<-scale(x=churn$Contacts)
churn$Yearly_equip_failure_z<-scale(x=churn$Yearly_equip_failure)
churn$Tenure_z<-scale(x=churn$Tenure)
churn$MonthlyCharge_z<-scale(x=churn$MonthlyCharge)
churn$Bandwidth_GB_Year_z<-scale(x=churn$Bandwidth_GB_Year)
view(churn)

#Determine range of values of outliers 
b_Children<-boxplot(churn$Children)
b_income<-boxplot(churn$Income)
b_outage<-boxplot(churn$Outage_sec_perweek)
b_contacts<-boxplot(churn$Contacts)
b_yearly<-boxplot(churn$Yearly_equip_failure)

#Determine quantity of outliers
children_query<-churn[which(churn$Children>6),]
income_query<-churn[which(churn$Income>75000),]
outage_query<-churn[which(churn$Outage_sec_perweek>20),]
contacts_query<-churn[which(churn$Contacts>5),]
yearly_query<-churn[which(churn$Yearly_equip_failure>2),]


#Remove unnecessary z-score columns
churn<-subset(churn, select= -c(Children_z, Age_z, Income_z, Outage_z, Contacts_z, Yearly_equip_failure_z, Tenure_z, MonthlyCharge_z, Bandwidth_GB_Year_z))

#Round ages so they are whole numbers
churn$Age<-round(churn$Age, digits=0)

#Consolidate Timezones into standard US Timezones
library(stringr)
#US/Eastern timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Marengo", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Vincennes", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Detroit", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Kentucky/Louisville", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Indianapolis", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Petersburg", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Winamac", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/New_York", "US/Eastern")
churn$Timezone<-str_replace(churn$Timezone, "America/Toronto", "US/Eastern")

#US/Mountain timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Boise", "US/Mountain")
churn$Timezone<-str_replace(churn$Timezone, "America/Ojinaga", "US/Mountain")
churn$Timezone<-str_replace(churn$Timezone, "America/Denver", "US/Mountain")

#US/Central timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Knox", "US/Central")
churn$Timezone<-str_replace(churn$Timezone, "America/Indiana/Tell_City", "US/Central")
churn$Timezone<-str_replace(churn$Timezone, "America/North_Dakota/New_Salem", "US/Central")
churn$Timezone<-str_replace(churn$Timezone, "America/Menominee", "US/Central")
churn$Timezone<-str_replace(churn$Timezone, "America/Chicago", "US/Central")

#US/Pacific timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Los_Angeles", "US/Pacific")

#US/Alaska timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Sitka", "US/Alaska")
churn$Timezone<-str_replace(churn$Timezone, "America/Nome", "US/Alaska")
churn$Timezone<-str_replace(churn$Timezone, "America/Anchorage", "US/Alaska")

#US/Arizona timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Phoenix", "US/Arizona")

#US/Hawaii timezones
churn$Timezone<-str_replace(churn$Timezone, "Pacific/Honolulu", "US/Hawaii")

#US/Puerto_Rico timezones
churn$Timezone<-str_replace(churn$Timezone, "America/Puerto_Rico", "US/Puerto_Rico")

#PCA code

#Import packages
library(plyr)
library(factoextra)

#Select columns of the dataframe and perform PCA
churn_pca.pca<-prcomp(churn[,c(9,10,11,19,23,42,43,44)], center=TRUE, scale=TRUE)
churn_pca.pca$rotation

#Create scree plot using eigen values
fviz_eig(churn_pca.pca, choice="eigenvalue", addlabels=TRUE)