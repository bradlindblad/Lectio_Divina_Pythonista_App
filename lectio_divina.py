#!/usr/bin/python3

print("""

 _           _   _             _ _       _             
| | ___  ___| |_(_) ___     __| (_)_   _(_)_ __   __ _ 
| |/ _ \/ __| __| |/ _ \   / _` | \ \ / / | '_ \ / _` |
| |  __/ (__| |_| | (_) | | (_| | |\ V /| | | | | (_| |
|_|\___|\___|\__|_|\___/   \__,_|_| \_/ |_|_| |_|\__,_|


""")


import os
import time



# Audio beep setup
duration = 0.1  # seconds
freq = 430  # Hzz


# -- FUNCTIONS ---------------------------------------

def playBell():
	os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


# -- START THE SESSION ---------------------------------

# Setup
input("Hit ENTER to start a lectio divina session")

time.sleep(3)

print('''
Step 1: Find a piece of scripture, anywhere from 1 sentence to 1 paragraph. 
Ideally, one where Jesus is doing something.


''')

input('''
Hit RETURN when you've found one
''')

time.sleep(1)


# -- Relax ---------------------------------------------
print('''
Sit down and relax...
''')

time.sleep(2)

print('''
Let's begin by relaxing. Do a 4-7-8 breathing for a bit.
''')

time.sleep(70)

playBell()

# -- Lectio ---------------------------------------------------
print('''
Part 1: Lectio (Reading)
Read the verse several times. Focus on one word or phrase intensely.
If anything jumps out to you, dwell on that.
''')

time.sleep(240)
playBell()

# -- Meditatio -------------------------------------------------
print('''
Part 2: Meditatio (Meditation)
Put yourself into the scene. Does this scripture apply to you today?
Ask the Holy Spirit to interpret this to you.
''')
time.sleep(240)
playBell()

# -- Oratio ----------------------------------------------------
print('''
Part 3: Oratio (Prayer)
Take all the thoughts, fears and ideas that have came up
and offer them to the Lord.
If there is a specific anxiety, offer it to the Lord.
If you are especially thankful, pray a prayer of thanksgiving.
''')

time.sleep(210)
playBell()

# -- Contemplatio ------------------------------------------------
print('''
Part 4: Contemplatio (Contemplation)
Sit in silence with God
''')

time.sleep(250)
playBell()

print('''
Now go out and live for Christ
''')

time.sleep(7)