'''
Consider the thirsty crow story where a thirsty crow identifies a jug 
with little water. It puts pebbles into the water to raise the level of 
water and drinks it. Assume that the initial reading of the jug is 'm1' ml 
and the crow can drink water if the level of water has come to 'm2' ml.  
There are two categories of pebbles small and big in the field. Small pebble 
can raise the level of water by 'x' ml and big pebble can raise the level of 
water by 'y' ml. There are 'n' small pebbles. Crow prefers to place small pebbles 
in jug and then only takes big pebbles. Write an algorithm and the Python code 
to determine the number of pebbles required to raise the water to ‘m2’ level. 
For example, if value of 'm1', 'm2','x','y' and 'n' are 54, 300, 10, 20, 10 
respectively then the number of pebbles required is 13.
'''

'''
ALGORITHM

--> Take input of m1, m2, x, y, and n
--> Initialize a variable total_pebbles to zero
--> Calculate difference in levels, diff = m2 - m1
--> small pebble needed , small_count = n if n * x < diff else diff // x
--> update variable total_pebbles
--> Remaining water level needed, rem_diff = diff - small_count * x
--> Big pebble neede , big_count = rem_diff // y
        --> IMPORTANT 
        --> still some levels needs to be raised -> 
        --> if(rem_diff % y < 10)  --> big_count += 1
--> update variable total_pebbles
--> Print the total number of pebbles required
'''

def num_pebbles(m1, m2, x, y, n):
    diff = m2 - m1

    total_pebbles = 0
    small_count = 0
    if(n * x < diff):
        small_count = n
    else:
        small_count = diff // x

    
    total_pebbles += small_count
    rem_diff = diff - small_count * x

    big_count = rem_diff // y

    # still water needs to raise more 
    if(rem_diff % y < 10):
        big_count += 1

    total_pebbles += big_count
    return total_pebbles


# User inputs
m1 = int(input('Enter initial water level : '))
m2 = int(input('Enter Required water level : '))
x = int(input('Enter water raise by small pebble : '))
y = int(input('Enter water raise by big pebble : '))
n = int(input('Enter count of small pebble : '))

pebbles_required = num_pebbles(m1, m2, x, y, n)

print(f"\nTotal pebbles required is {pebbles_required}")
