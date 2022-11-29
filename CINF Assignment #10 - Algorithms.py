#CINF Assignment #10 - Algorithms
#This is James Gillanders' code

#For this program, we will be creating two functions to call on for sorting a list of values. 
#One will be a sorting algorithm, specifically Bubble Sort, and the other will be a kind of search/return 
#algorithm that can pick out any value the user wants. 


print("\nWelcome to the algorithm machine, would you like to sort or search this list?")

print([ 4, 3, 20, 35, 64, 103, 88, 14, 430, 48, 1, 5, 34, 82, 26, 28, 800 ])

master_control = input("Search or Sort?: ")
if master_control == "Sort":
#First function for bubble sort, which will implement time complexity. In short, bubble algorithms 
#sort based on adjacency, so if a number next to another is larger or smaller, it will sort accordingly. 
 def bubbles(arr):
#Determining the length of the list
    
    measure = len(arr)

    #Next we can use a loop to go through all the numbers in 
    #our list
    for i in range(measure):
        for j in range(0, measure - i - 1):
            #This is our bubble sort in action, with our range being determined first
            #and the actual swap coming next. 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

 sort_confirm = input("Would you like to sort the list? Yes/No: ")
 if sort_confirm == "Yes":
    #Our lengthy, randomly generated number sequence.
    arr = [ 4, 3, 20, 35, 64, 103, 88, 14, 430, 48, 1, 5, 34, 82, 26, 28, 800 ]

    bubbles(arr)


    print("This list is sorted like so: ")
    for i in range(len(arr)):
     print("%d" % arr[i])
    #Here we use %d, which is a fill-in for digits until they are processed. Then we use the modulus to 
    #divide and return the remainder. 
 elif sort_confirm == "No":
    print("This list is unsorted")


#Second function for returning an element from our same list. This will be a linear search, which iterates the items 
#in a list one by one
elif master_control == "Search":
 def linear(val, seek):
   watchpoint = 0
   resolution = False
#We have to match our inputted values to the Booleans
   while watchpoint < len(val) and resolution is False:
      if val[watchpoint] == seek:
         resolution = True
      else:
         watchpoint = watchpoint + 1
   return resolution
 arr = [ 4, 3, 20, 35, 64, 103, 88, 14, 430, 48, 1, 5, 34, 82, 26, 28, 800 ]
 search_confirm = input("Would you like to search the list?: ")
 if search_confirm == "Yes":
    print("Enter a value you wish to search for: ")
    print(linear(arr, input()))
    #Seek becomes an input so the user can search for the number they want.
 elif search_confirm == "No":
    print("The list is not searched")
  

    