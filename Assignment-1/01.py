'''
A team of authorities designed by Govt. of India to conduct a survey on Colleges. 
Let us assume 'n' number of colleges. They were asked to rank the colleges based 
on 3 different parameters. The parameters are facilities, academics and infrastructure. 
Maximum score in each parameter is as follows.
Facilities=25
Academics=50
Infrastructure=25
At the end of the survey the scores of the individual parameters are added up to get 
the total score and the colleges are ranked based on the score. The college that scores 
the highest score is ranked first.Next highest score is given the rank second and so on. 
Write a program to read the scores of the three parameters for each college, store the scores in a list. 
Make a list of individual score list for ten colleges. 
Find the total score for all ten colleges, and sort them. 
Print the Total score in the sorted (Descending) order. 
You have to use any sorting method for sorting.
'''

# Taking college inputs for 5 colleges
def read_scores():
    facilities = int(input("Enter the score for facilities (out of 25): "))
    academics = int(input("Enter the score for academics (out of 50): "))
    infrastructure = int(input("Enter the score for infrastructure (out of 25): "))
    return [facilities, academics, infrastructure]

# Creating list of lists
score_lists = []
for i in range(5):
    print("Enter scores for College" , i+1 , ": ")
    scores = read_scores()
    score_lists.append(scores)

# Total scores 
total_scores = []
for scores in score_lists:
    total_score = sum(scores)
    total_scores.append(total_score)

# Sort the total scores in descending order
total_scores.sort(reverse=True)

# Print the sorted total scores
print("\n")
print("Sorted Total Scores:")
for score in total_scores:
    print(score , end=" ")
