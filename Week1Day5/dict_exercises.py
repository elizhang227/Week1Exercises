
# CODE ALONG

# digitalcrafts = {
#     'US': {
#         'Georgia': {
#             'Atlanta': '3423 Pidemont Rd NE #415'
#         }
#         # 'Texas': {
#         #     'Houston': '3302 Canal St.'
#         # }
#     }
# }

# # Add new campus
# digitalcrafts['US']['Florida'] = {
#     'Orlando': 'Communicore Epcot'
# }

# # Adds new key in digitalcrafts
# digitalcrafts['UK'] = {}
# # Adds new key (Surrey) inside existing key (UK)
# digitalcrafts['UK']['Surrey'] = {
#     'Croydon' : '420 High Street'
# }

# print(digitalcrafts)

# Exercise #1

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# 1. Prints Elizabeth's number
#print(phonebook_dict['Elizabeth']) 

# 2. Adds key Karem with number as the value and prints
# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

# 3. Delete Alice's phone entry
# del phonebook_dict['Alice']
# print(phonebook_dict)

# 4. Change Bob's number
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

# 5. Print all phone entries
# print(phonebook_dict)

# Exercise #2

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# 1. email of Ramit
# print(ramit['email'])

# 2. first interest of Ramit
# print(ramit['interests'][0])

# 3. email address of Jasmine
# print(ramit['friends'][0]['email'])

# 4. second of Jan's two interests
# print(ramit['friends'][1]['interests'][1])

# Exercise #3
# word = input('Please enter a word: ')
# count = {}

# for letter in word:
#     if letter in count:
#         count.append(letter)
#     elif letter not in count:
#         count[letter] = 1

# print(count)

# Letter Summary

# def letter_counter(str):
#     dict = {}
#     for i in str:
#         if i in dict.keys():
#             dict[i] += 1
#         elif i not in dict.keys():
#             dict[i] = 1
#     return dict

# print(letter_counter(input('Please enter a word: ')))

### Word Summary ###

# sentence = input('Please enter a sentence: ')
# split = sentence.split()
# dict = {}

# for word in split:
#     if word in dict:
#         dict[word] += 1
#     elif word not in dict:
#         dict[word] = 1

# print(dict)

