#Script and Text File Created By Bhavya Shah
# Data is based on 2018 crime statistics published by CP24 and reported by Narcity
# Intended to assist New Residents to Toronto when picking a neighbourhood to live in
import os
import sys

#Read the file line by line
filename = 'toneighbourhood.txt'
with open(filename) as f:
    content = f.readlines()

#  remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

my_list = []
striped = []

#Remove any whitespace inside each list element
for i in content:
	j = i.replace(' ','')
	striped.append(j)
for item in striped:
	my_list.append(item.split(','))

#Create a list of lists for each line/neighbourhood division in file
toronto = [];
for element in my_list:
	toronto.append(element)

#Function Returns a Division list if the neighbourhood is in it
def in_list(list_of_lists, item):
	#print (item)
	for each_list in list_of_lists:
		#print(each_list)
		if item in each_list:
			
			return each_list
	return 1

def main():
	counter = True 
	
	print('***********************************************************')
	print('Stay Safe Toronto')
	print('***********************************************************')
	
	while counter != False:	
		user_choice = input('Enter your neighbourhood or type q to quit:')
		if user_choice != 'q':
			strip_user_choice = user_choice.replace(" ","")

			returned_list=in_list(toronto,strip_user_choice)

			if returned_list == 1:
				print('The neighbourhood '+ user_choice+ " is not in our data")
				print('***********************************************************')

			else:
				print("The neighbourhood "+ user_choice+ " is located in division "+returned_list[1]+" which ranks"+ " number "+ returned_list[0]+ " in crime out of the top 17 crime divisions")
				print("Total crimes in the division were: "+ returned_list[2]+" with most common occurences of "+ returned_list[3])
				print('***********************************************************')
				
		else:
			print('Thanks for using StaySafeTO!')
			counter = False

main()