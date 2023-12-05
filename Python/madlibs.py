
with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_ow = -1

t_start = "<"
t_end = ">"
#this finds words in the text file which have <> around them
for i, char in enumerate(story):
    if char == t_start:
        start_ow = i

    if char == t_end and start_ow != -1:
        word = story[start_ow: i + 1]
        words.add(word)
        start_ow = -1
    
answers = {}

for word in words:
    answer = input("Enter a " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
quit()