#this is  telling python to remmember the types of people
types_of_people=10
#this is showng us a sentance that tells us how many types of people
x=f"there are {types_of_people} types of people"
#this is telling python to remmember the word binary under the word binary
binary='binary'
#this is telling python to remmember 'don't' under do_not
do_not="don't"
#this telling us that not every type knows binary
y=f"people who know {binary} and people who {do_not}"
#this is telling us again how many types of people there are
print(x)
#this is telling us again that not everyone knows binary
print(y)
#this telling us that they said  that there are 10 types
print(f"I said:'{x}'")
#this telling us that they said that not every one knows binary
print(f"I also said:'{y}'")
#this is telling python to remmember false under hilarious
hilarious=False
#this tells python that eny time someone types in joke_evalouation it says  'ins't that 
# joke so funny'
joke_evaloation="isn't that joke so funny?! {}"
#this is telling us that the joke is not funny
print(joke_evaloation.format(hilarious))
#this is telling python half of a sentance
w=("this the left side of...")
#this is telling python the other half of the sentance
e=("a string with a right side.")
#this is telling us the sentance put together
print(w+e)      