"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []
story.append(words[0])
story.append(words[2])
story.append(words[7])
story.append(words[9])
story.append(words[3])
story.append(words[15])
story.append(words[10])
story.append(words[8])
story.append(words[4])

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))