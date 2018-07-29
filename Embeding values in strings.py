# If you want to display a mrddage using the contents of a vatiable, you can embed values in a string using %s.
myscore = 1000
message = 'I scored %s points'
print(message % myscore)
joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
# Can also use more than one placeholder
nums = 'What did the number %s say to the number %s? Nice belt!!'
print(nums % (0,8))