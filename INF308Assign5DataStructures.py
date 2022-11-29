#CINF 308 Assignment 5 - Dictionaries and Tuples
#This is James Gillanders' code

#This program stores the data of a social media profile into the specified data structure, being a list, tuple, and dictionary respectively.
#We will utilize a few different techniques to make this work, but the layout will still be fairly straightforward. 

#First question asking for basic user information
print("\nThank you for making an account with us! We will ask for some basic information to get you started.")
print("Enter your name, birthday, email, and username: ")
#Puts strings into a list
profile_list = [str(i) for i in input().split()] #.split() so everything stays spaced out.
print(profile_list)

#Next question is for the tuples
print("\nGreat, we are almost done.")
print("Tell us about yourself! Your favorite movies, music, and whatever else!: ")
#This allows the user to put in as many hobbies as they want, then once they are done they enter "DONE"
hobby_tuple = input("\nEnter your number of hobbies, then say what they are! ")
interest_question = ()

#The loop could go on forever, however giving a number first lets the user decide how many they want. They will all go into a tuple at the end.
if hobby_tuple != 'DONE':
    interest_question = tuple(hobby_tuple)
while True:  
    #"DONE" is the escape command, had to include one somewhere
    if hobby_tuple != 'DONE':
       hobby_tuple = input("Enter some hobbies! When finished input \"DONE\": ")
    if hobby_tuple != "DONE":
        interest_question = interest_question + (hobby_tuple,)  
    else:
         break

print(interest_question)

#This question is for the dictionary, I went for a security scenario where the user decides a value associated with a term. This is saved and hypothetically used for safety on login.
print("\nLastly, for your own security, enter a security prompt and then an answer.")
#This takes a single value
sec_prompt = input("Enter a name and then a value associated with it: ")
security_questions = dict(x.split() for x in sec_prompt.splitlines())
print(security_questions)
#Then a compilation of all the data. 
print("\nFinally, we are done! Below will be your compiled profile data")
param1 = "Your information: "
param2 = "Your hobbies & interests: "
param3 = "Your safety codes: "
#I know this was not necessary but I figured it would be representative of how a real social media account would ask you if everything looked good. 
#I was originally going to add another conditional at the end in case the user wanted to change anything else, but I might save that for later. 
user_info = print([(param1 + ' , '.join(profile_list)), (param2 + " , ".join(interest_question)), (param3 + ' '.join(security_questions))])
#Used .join() to combine the data structures with variables. 
print(user_info)

    


