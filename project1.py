import csv

def uhf_splitter(uhf): #splits the uhf strings into a set of singular uhf 3-digit integers
  if len(uhf) == 0:
    return []
  return [int(uhf[:3])] + uhf_splitter(uhf[3:])

def data_analysis(file1, file2):
  
  measurements_file = open(file1, 'r')
  measurements_reader = csv.reader(measurements_file)
  id_dict = {} #dictionary a)1
  date_dict = {} #dictionary a)2
  
  for line in measurements_reader:
    for uhf in uhf_splitter(line[0]):
      if uhf not in id_dict: #appends list to id_dict if key not yet define
        id_dict[uhf] = [] 
      id_dict[uhf].append(tuple([uhf]+line[1:])) #appends into list
      if line[2] not in date_dict: #appends list to date_dict if key not yet defined
          date_dict[line[2]] = []
      date_dict[line[2]].append(tuple([uhf]+line[1:])) #appends into list
    
  """
  for key,value in id_dict.items():
    print(key,value)
  for key,value in date_dict.items():
    print(key,value)
  """
  
  measurements_file.close()
  
  uhf_file = open(file2, 'r')
  uhf_reader = csv.reader(uhf_file)
  zip_dict = {} #dictionary b)1
  borough_dict = {} #dictionary b)2
  
  for line in uhf_reader:
    uhf_split = uhf_splitter(line[2])
    for zip in line[3:]: #appends uhfs into zip_dict
      if zip not in zip_dict: #creates key if key does no exist
        zip_dict[zip] = []
      for uhf in uhf_split:
        if uhf not in zip_dict[zip]: #appends uhf into list for respective key if uhf is not already there
          zip_dict[zip].append(uhf)
    borough = line[0]
    if borough not in borough_dict: #creates key if key does not exist
      borough_dict[borough] = []
    for uhf in uhf_split:
      if uhf not in borough_dict[borough]: #appends uhf into list for respective key if uhf is not already there
        borough_dict[borough].append(uhf)
  
  """
  for key,value in zip_dict.items():
    print(key,value)
  for key,value in borough_dict.items():
    print(key,value)
  """
  
  uhf_file.close()
  return [id_dict, date_dict, zip_dict, borough_dict]

def user_query(file1, file2, mode):
  id_dict, date_dict, zip_dict, borough_dict = data_analysis(file1, file2)
  ans = input("Do you want to search the data by (z)ipcode, (U)HF, (b)orough, or (d)ate?")
  #keeps prompting user for input while input is not valid:
  while ans.lower() not in ('z','u','b','d'):
    ans = input("Wrong input. Do you want to search the data by (z)ipcode, (U)HF, (b)orough, or (d)ate? ")
  result = []
  #if the user wants to search by zipcode
  if ans.lower() == "z":
    zip = input("Please enter a zipcode: ")
    while zip not in zip_dict.keys():
      zip = input("Wrong input. Please enter a zipcode: ")
    # assigns uhf list corresponding to the inputted zipcode to the variable uhf_list
    uhf_list = zip_dict[zip]
    # for every uhf in the list, measurements is the corresponding list of tuples 
  
    for uhf in uhf_list:
      measurements = id_dict[uhf]
      for line in measurements:
        if mode == 'p': #if mode is p, print the measurements
          print(f"{line[2]} UHF {line[0]} {line[1]} {line[3]} mcg/m^3")
        elif mode == 'r': #if mode is p, append the measurements to result
          result.append(line)
        else:
          print("Wrong mode.") # if mode is not p or r, print wrong mode message
  elif ans.lower() == "u":
    uhf = int(input("Please enter an UHF: "))
    while uhf not in id_dict.keys():
      uhf = int(input("Wrong input. Please enter an UHF: "))
#finds list of measurement tuples in id_dict and assigns it to the measurements variable
    measurements = id_dict[uhf] 
    for line in measurements:
      if mode == 'p':
        #print formatted measurements
        print(f"{line[2]} UHF {line[0]} {line[1]} {line[3]} mcg/m^3") 
      elif mode == 'r':
        result.append(line)
      else:
        print("Wrong mode.")
  elif ans.lower() == "b": #search by borough
    borough = input("Please enter a borough: ")
    while borough not in borough_dict.keys():
      borough = input("Wrong input. Please enter a borough: ")
      # list of uhfs corresponding to the entered borough is assigned to uhf_list
    uhf_list = borough_dict[borough] 
    for uhf in uhf_list:
      measurements = id_dict[uhf]
      for line in measurements:
        if mode == 'p':
          #print formatted measurements
          print(f"{line[2]} UHF {line[0]} {line[1]} {line[3]} mcg/m^3") 
        elif mode == 'r':
          result.append(line)
        else:
          print("Wrong mode.") # if mode is not p or r, print wrong mode message
  elif ans.lower() == "d": #search by date
    date = input("Please enter a date: ")
    while date not in date_dict.keys():
      date = input("Wrong input. Please enter a date: ")
    measurements = date_dict[date]
    for line in measurements:
      if mode == 'p':
        #print formatted measurements
        print(f"{line[2]} UHF {line[0]} {line[1]} {line[3]} mcg/m^3") 
      elif mode == 'r':
        result.append(line)
      else:
        print("Wrong mode.") # if mode is not p or r, print wrong mode message
  if mode == 'r':
    return result