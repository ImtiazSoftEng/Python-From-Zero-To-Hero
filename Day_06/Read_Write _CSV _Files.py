import csv
with open('Day_06/people.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#Write to CSV Files with Python
with open('Day_06/protagonist.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Imtaz Ali',25,'New York'])
    writer.writerow(['Ahmad',30,'Los Angeles'])
    writer.writerow(['Abbas',35,'Chicago'])
#Now read the file again to see the changes
with open('Day_06/protagonist.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#Using Python Pandas to Handle CSV Files
#Read CSV Files
import pandas as pd
 
data=pd.read_csv('Day_06/people.csv')
print(data)


#Write to a CSV Files
#Create a DataFrame
df=pd.DataFrame([['Uzma',20],['Ali',25],['Sara',30]],columns=['Name','Age' ])
df.to_csv('Day_06/protagonist_pandas.csv',index=False)

#Now read the file again to see the changes
data=pd.read_csv('Day_06/protagonist_pandas.csv')
print(data)