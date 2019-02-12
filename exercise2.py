documentary = 'March of the penguins'
drama = 'Shawshak Redemption'
comedy = 'Horrible Bosses'
dramedy = 'Juno'

print('Please rate documentaries from 1-5.')
documentaries_rating = int(input())
print('Please rate dramas from 1-5')
drama_rating = int(input())
print('Please rate comedies from 1-5?')
comedy_rating = int(input())

if (documentaries_rating >= 4):
    print('I would recommend {}!'.format(documentary))
elif (documentaries_rating <= 3) and (drama_rating >= 4) and (comedy_rating >= 4):
    print("I would recommend {}!".format(dramedy))
elif (drama_rating >= 4):
    print("I would recommend {}!".format(drama))
elif (comedy_response >= 4):
    print("I would recommend {}!".format(comedy))
else:
    print("Maybe movies aren't for you")
