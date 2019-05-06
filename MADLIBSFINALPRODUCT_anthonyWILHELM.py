story_swim = """

First, you need a {clothing1}. Make sure it's comfortable and not {adjective1}.
First lets start out at the {adjective2} end of the pool. Dip your {bodypart1} in the {liquid1}
until you're completely {adjective3}. Then once you're in, start with the {animal1} paddle.
Kick your {bodypart2} and {bodypart3} like you're whipping {liquid2}. You should start to float, if not,
{verb1} your muscles and try again. Once you're body is {verb2} freely, lift your left {bodypart4} and
place it in front of your {bodypart5}. Then do the same with your right {bodypart6}.
At the same time, kick your {bodypart7} like you're a {animal2} trying to {verb3}.
You should see your body starting to move {direction1}, keep your {bodypart8} in the air at all
times and wearing some {noun1} can protect your {bodypart9}. {noun2} and {noun3} plugs are
optional as well. Swim a few strokes around the {noun4} until you get the hang of it.
Next, we can try diving off the {noun5}. Pretend you're an {animal3} flying freely through the {earthlysubstance1}.
It's a lot of fun! Once you go under water, remember to kick but stay {emotion1}. Soon, you'll be able
to float on {liquid3} without effort. Swimming is {adjective4}, {adjective6} and {adjective5}. I hope this
step-by-step guide helped you become the {adjective7} swimmer!"""

story_cows = """

There was once a {adjectivecow1} cow that said "{exclamationcow1}" whenever she was milked.
Her milk was very {adjectivecow2}, and whoever drunk it just wanted to {verbcow1}.
The man who owned the cow bought her for {numbercow1} {colorcow1} {nouncow1}. He thought to himself "exclamationcow2"
I never thought I would buy a cow like this. He {adverbcow1} rushed the cow home
and put it under his {adjectivecow3} {nouncow2}. Then called all of his {adjectivecow4} friends and
invited them over to have a {adjectivecow5} cow party. """

story_potato = """

One time {namepot1} the potato decided to {verbpot1} a {nounpot1}. He invited all of his {nounpot2} and {nounpot3}.
It was going to be so much fun! At {timepot1} o'clock {namepot2}, {namepot3}, and {namepot4} arrived.
Soon, even more {nounpot4} arrived. {namepot5} the potato yelled " {exclamationpot1} " Once many people arrived.
It was amazing. {adjectivepot1}, it went downhill {adverbpot1}. {namepot6} had failed and he was no longer going
to {verbpot2} any {nounpot5}. That {timeofday1}, {namepot7} went to bed, disappointed of his actions.
He dreamt of {nounpot6} that night. """

mad = dict()

def getword(word_type, storage, key):
    storage[key] = input(f"Please give me a {word_type}: ")

def get_swim():
    getword('piece of clothing', mad, 'clothing1')
    getword('adjective', mad, 'adjective1')
    getword('adjective', mad, 'adjective2')
    getword('body part', mad, 'bodypart1')
    getword('liquid', mad, 'liquid1')
    getword('adjective', mad, 'adjective3')

    getword('animal', mad, 'animal1')
    getword('body part, plural', mad, 'bodypart2')
    getword('body part, plural', mad, 'bodypart3')
    getword('liquid', mad, 'liquid2')
    getword('verb', mad, 'verb1')
    getword('verb-ending in ING', mad, 'verb2')

    getword('body part', mad, 'bodypart4')
    getword('body part', mad, 'bodypart5')
    getword('body part', mad, 'bodypart6')
    getword('verb', mad, 'verb3')
    getword('animal', mad, 'animal2')
    getword('body part, plural', mad, 'bodypart7')

    getword('direction-backwards, sideways, etc', mad, 'direction1')
    getword('body part', mad, 'bodypart8')
    getword('noun, plural', mad, 'noun1')
    getword('body part, plural', mad, 'bodypart9')
    getword('noun, plural', mad, 'noun2')
    getword('noun', mad, 'noun3')

    getword('noun', mad, 'noun4')
    getword('noun', mad, 'noun5')
    getword('animal', mad, 'animal3')
    getword('earthly substance-water, air, fire, smoke, etc', mad, 'earthlysubstance1')
    getword('emotion', mad, 'emotion1')
    getword('liquid', mad, 'liquid3')

    getword('adjective', mad, 'adjective4')
    getword('adjective', mad, 'adjective5')
    getword('adjective', mad, 'adjective6')
    getword('adjective-ending in EST', mad, 'adjective7')


def get_cows():
    getword('adjective', mad, 'adjectivecow1')
    getword('exclamation', mad, 'exclamationcow1')
    getword('adjective', mad, 'adjectivecow2')
    getword('verb', mad, 'verbcow1')
    getword('number', mad, 'numbercow1')
    getword('color', mad, 'colorcow1')

    getword('noun, plural', mad, 'nouncow1')
    getword('exclamation', mad, 'exclamationcow2')
    getword('adverb', mad, 'adverbcow1')
    getword('adjective', mad, 'adjectivecow3')
    getword('noun', mad, 'nouncow2')
    getword('adjective', mad, 'adjectivecow4')

    getword('adjective', mad, 'adjectivecow5')

def get_potato():
    getword('name', mad, 'namepot1')
    getword('verb', mad, 'verbpot1')
    getword('noun', mad, 'nounpot1')
    getword('noun, plural', mad, 'nounpot2')
    getword('noun', mad, 'nounpot3')
    getword('time, just the number', mad, 'timepot1')

    getword('name', mad, 'namepot2')
    getword('name', mad, 'namepot3')
    getword('name', mad, 'namepot4')
    getword('noun, plural', mad, 'nounpot4')
    getword('name', mad, 'namepot5')
    getword('exclamation', mad, 'exclamationpot1')

    getword('adjective', mad, 'adjectivepot1')
    getword('adverb', mad, 'adverbpot1')
    getword('name', mad, 'namepot6')
    getword('verb', mad, 'verbpot2')
    getword('noun, plural', mad, 'nounpot5')
    getword('time of day', mad, 'timeofday1')

    getword('name', mad, 'namepot7')
    getword('noun, plural', mad, 'nounpot6')



chosen_story = None
chosen_get = None

print("Welcome to Super Mad Libs!\nBy: Anthony Wilhelm CIS104A\n")
choice = int(input("Please pick your story. Select 1 for a Swimming story, select 2 for a Cow story, Select 3 for a potato story!"))

if choice == 1:
    chosen_story = story_swim
    chosen_get = get_swim

if choice == 2:
    chosen_story = story_cows
    chosen_get = get_cows

if choice == 3:
    chosen_story = story_potato
    chosen_get = get_potato

chosen_get()

print(chosen_story.format(**mad))
print("\n")
print("I hope you enjoyed your story! Thank you for playing Super Mad Libs by Anthony Wilhelm")