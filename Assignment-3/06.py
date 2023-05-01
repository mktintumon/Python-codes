'''
Word_Antakshri is a spoken modernparlor game played in India. The game
can be played by two or more people and is a popular as a group activity.The
first singer has to sing one complete line of song and stops at a point. The last
word sung by the previous player is then used by the nextsinger to sing
anothernewsong, starting with that word. This process continues until a
person or a team that can not come up with the right consonant with in a
time constraint. Given the lines of song sung by the first and the second
player, design a flowchart and write the Python code to print ‘Pass’ or ‘Stop’
word. If rules of the game is followed by the second player then print “Pass”
otherwise print “Stop”. For example, if the line sung by the first player is “One
two three” and the line sung by the second player is “Three four five” then
print Pass. If the line sung by the first player is “One two” and the line sung
by the second player is “Three four five” then print Stop. Make the process
to be case insensitive.
'''


flag = True

while(flag):
    first_line = input("Enter the first line of song: ").lower()
    second_line = input("Enter the second line of song: ").lower()

    last_word = first_line.split()[-1]
    first_word = second_line.split()[0]

    # Checking the rule of Antakshri
    if last_word == first_word:
        print("Pass\n")
    else:
        print("Stop\n")
        flag = False

