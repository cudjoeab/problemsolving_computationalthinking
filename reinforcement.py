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

# Save the direction of train 111 into a variable.

for train in train_schedule:
    if train['train'] == '111':
       direction = train['direction'] 

# save the frequency of train 80B into a variable

for train in train_schedule:
    if train['frequency_in_minutes'] == '30':
       mins= train['frequency_in_minutes'] 

#save the direction of train 610 into a variable 
for train in train_schedule:
    if train['frequency_in_minutes'] == '30':
       mins= train['frequency_in_minutes'] 

