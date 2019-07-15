train_schedule = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# 1 Save the direction of train 111 into a variable.

for train in train_schedule:
    if train['train'] == '111':
       direction = train['direction'] 


#2  save the frequency of train 80B into a variable

for train in train_schedule:
    if train['frequency_in_minutes'] == '30':
       mins= train['frequency_in_minutes'] 

#3 save the direction of train 610 into a variable

for train in train_schedule:
    if train['frequency_in_minutes'] == '30':
       mins= train['frequency_in_minutes'] 

#4 Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.

northbound_trains = []
for vehicle in train_schedule:
    name = vehicle['train']
    direction = vehicle['direction']
    if direction == 'north':
        northbound_trains.append(name) 

print(northbound_trains)

#5 Eastbound trains 

eastbound_trains = []
for vehicle in train_schedule:
    name = vehicle['train']
    direction = vehicle['direction']
    if direction == 'east':
        eastbound_trains.append(name) 

print(eastbound_trains)

#6 DRY up code for 4 and 5 

def train_direction(train_schedule, direction):
    for vehicle in train_schedule: 
        name = vehicle['train']
        train_direction = vehicle['direction']
        if train_direction == direction:
            return name 

print(train_direction(train_schedule, 'north'))
print(train_direction(train_schedule, 'east'))

#7 Adding a new train, and find departure time 

train_schedule[4]['first_departure_time'] = 17

print(train_schedule[4])

#8 rearranging code 
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]




trains_by_frequency = {}
for train in trains:
    name = train['train']
    freq = train['frequency_in_minutes']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)    
    else:
        trains_by_frequency[freq] = [name]
        

  
print(trains_by_frequency)





