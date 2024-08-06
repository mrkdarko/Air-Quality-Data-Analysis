import project1

print("To get the highest and lowest pollution in zip code 10027, please select 'z' and then '10027'.")
result = project1.user_query('air_quality.csv', 'uhf.csv', 'r')
max = 0
min = 100000

for line in result:
    if float(line[3]) > max: 
      max = float(line[3]) #find the tuple with the highest pollution 
    if float(line[3]) < min:
      min = float(line[3]) #find the tuple with the lowest pollution

print("\na) Maximum pollution in zip code 10027:", max)
print("\na) Minimum pollution in zip code 10027:", min)


max = 0
max_line = ()
data_dict = project1.data_analysis('air_quality.csv', 'uhf.csv')[1]
for data, measurement in data_dict.items():
  if data[-2:] == '19': #check dates which end with 19
    for line in measurement:
      if float(line[3]) > max: #find key with highest pollution
        max = float(line[3])
        max_line = line
print("\nb) The UHF id with the worst pollution in 2019 was:", max_line[0], "\nThe pollution was:", max) #find the uhf of the highest pollution

print("\nTo find the average pollution in Manahattan in 2008 and 2019 please select 'b' then 'Manahattan'.")
result = project1.user_query('air_quality.csv', 'uhf.csv', 'r')
pollution_in_08 = []
for line in result:
  if line[2][-2:] =='08': #find dates which end with 08 for Manhattan
    pollution_08 = float(line[3])
    pollution_in_08.append(pollution_08) #create list of pollution in 2008
avg_poll_08 = sum(pollution_in_08)/len(pollution_in_08) #find the average pollution in 08
print("\nc) The average pollution in Manhattan in 2008 is:", round(avg_poll_08,3))

pollution_in_19 = []
for line in result:
  if line[2][-2:] =='19': #find dates which end with 19 for Manhattan
    pollution_19 = float(line[3]) 
    pollution_in_19.append(pollution_19) #create list of pollution in 2019
avg_poll_19 = sum(pollution_in_19)/len(pollution_in_19) #find the average pollution in 19
print("\nc) The average pollution in Manhattan in 2019 is:", round(avg_poll_19, 3))

#find the range of pollution in 2010 for Bronx
print("\nd) To get the range of pollution in 2010 in Bronx, please select 'b' and then 'Bronx'.")
result = project1.user_query('air_quality.csv', 'uhf.csv', 'r')
pollution_in_10 = []
for line in result:
  if line[2][-2:] =='10': #find dates which end with 10 for Bronx
    pollution_10 = float(line[3])
    pollution_in_10.append(pollution_10) # create list of pollution in 2010
lowest = pollution_in_10[0]
for pollution in pollution_in_10:
  if pollution < lowest: #find the lowest pollution in 2010
    lowest = pollution
highest = pollution_in_10[0]
for pollution in pollution_in_10:
  if pollution > highest: #find the highest pollution in 2010
    highest = pollution
range = round(highest - lowest,3)
print("The range of pollution in Bronx in 2010 is :", range)

#find the median of all the pollution in East Harlem throughout the years
print("\nd) To get the median pollution in East Harlem, please select 'b' and then 'Manhattan'.")
result = project1.user_query('air_quality.csv', 'uhf.csv', 'r')
pollution_in_east_harlem = []
for line in result:
  if line[1] =='East Harlem': #find pollution in East Harlem
    pollution_east_harlem = float(line[3])
    pollution_in_east_harlem.append(pollution_east_harlem) #create list of pollution in East Harlem
pollution_in_east_harlem.sort() #arrange from lowest to highest
median = pollution_in_east_harlem[len(pollution_in_east_harlem)//2]
print("Median pollution in East Harlem:", median)
