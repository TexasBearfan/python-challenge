import csv#imports csv library

filepath='C:/Users/jacqu/vu_bootcamp/VU-VIRT-DATA-PT-11-2023-U-LOLC/03-Python/Starter_Code/PyBank/Resources/budget_data.csv'
#defines file path
row_count=0#variable for rows/months
total=int(0)#variable for total
bignum=int(0)#variable for greatest inc
lownum=int(0)#variabel for greatest Dec
bigmonth=" "#string for the month of Greatest inc
lowmonth=" "#string for the month of Greatest dec
with open(filepath) as csv_file:#opens file and defines it as csv_file
    csv_reader=csv.reader(csv_file,delimiter=",")#defines the csv reader 
    csv_header=next(csv_file)#saves the header as a seperate variable
    for row in csv_reader:#for loop to run through the file
       row_count+=1#increment to count for loops/rows/months
       num=int(row[1])#sets current rows num to num
       month=str(row[0])#sets current months to month
       total=total+num#adding the current num to the total
       if num>bignum:
        bignum=num#setting current num to Greatest Inc
        bigmonth=month#saving current month for display with Greatest inc
       if num<lownum:
        lownum=num#setting current num to Greatesr dec
        lowmonth=month#saving current month for dsiplay with Greatest dec
av=total/row_count#logic for the Average Change
total_format="${:,.2f}".format(total)#format the total to currency form
av_format="${:,.2f}".format(av)#format the average to currency form
bignum_format="${:,.2f}".format(bignum)#format the Greatest Inc to currency form
lownum_format="${:,.2f}".format(lownum)#format the Greatest dec to currency form
print("Financial Analysis")
print(f"Total Months: {row_count}")
print(f"Total: {total_format}")
print(f"Average Change: {av_format}")
print(f"Greatest Increase in Profits: {bigmonth} ({bignum_format})")
print(f"Greatest Decrease in Profits: {lowmonth} ({lownum_format})")
#print statements for display of data
output_path="C:/Users/jacqu/vu_bootcamp/VU-VIRT-DATA-PT-11-2023-U-LOLC/03-Python/Starter_Code/PyBank/Resources/pybank.csv"
#defines output path
with open(output_path,'w') as csv_file:#opening file and defining as csv_file
    csvwriter=csv.writer(csv_file)#defining the csv writer
    csvwriter.writerow([f"Financial Analysis\nTotal Months: {row_count}\nTotal: {total_format}\nAverage Change: {av_format}\nGreatest Increase in Profits: {bigmonth} ({bignum_format})\nGreatest Decrease in Profits: {lowmonth} ({lownum_format})"])
        #print statement for csv file \n signifies a line break