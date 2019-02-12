documentary = 'March of the penguins'
drama = 'Shawshak Redemption'
comedy = 'Horrible Bosses'
dramedy = 'Juno'

print('Do you like documentaries?')
documentaries_response = input().lower()[0] #returns first lowercase letter of string (y or n)
print('Do you like dramas?')
drama_response = input().lower()[0]
print('Do you like comedies?')
comedy_response = input().lower()[0]

if (documentaries_response == 'y'): #if they choose doc then it recommends
    print('I would recommend {}!'.format(documentary))
elif (documentaries_response == 'n') and (drama_response == 'y') and (comedy_response == 'y'): #if they dont like docs AND like dramas and comedies - print this
    print("I would recommend {}!".format(dramedy))
elif (drama_response == 'y') and (comedy_response == 'n'):
    print("I would recommend {}!".format(drama))
elif (drama_response == 'n') and (comedy_response == 'y'):
    print("I would recommend {}!".format(comedy))
else: #used to end the loop and suggest a book instead
    print("Try a book instead")
