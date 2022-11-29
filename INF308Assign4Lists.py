#CINF Assignment 4 - List Manipulation

#This code will be pretty simple, we will conduct a programmning languages survey, asking a set
#of simple questions in the style of a survey. Eventually, this will culminate in lists of languages
#that utilize methods and can include whichever elements the user desires.

#Determine the lists

knownLangs = []

wantLang = []

#Input prompts
surveyQ1 = str(input("Welcome to our programming languages survey! How many languages do you know? : "))
#1st list methods, .split()
knownLangs = [str(item) for item in input("Enter the languages you know: ").split()]

wantLang = [item for item in input("Enter the languages you want to learn: ").split()]

#This is where we will combine items between lists now that we have established the user interface.
print("You are familiar with these programming languages: " + str(knownLangs))
print("You want to learn these languages: " + str(wantLang))
 
#2nd list method
knownLangs.extend(wantLang)

print("Here is your compiled programming language data! " + str(knownLangs))
#Combine the lists

#Next question
surveyQ2 = int(input("How many years have you been programming? : "))

yearsExp = surveyQ2
#Combine the data
languageData = "Your languages: " + str(knownLangs), "Years of Experience: " + str(yearsExp)
#The final input asking to see the data again
startOver = str(input("Would you like to see this data again? Y/N: "))
#Function uses a for loop to do something again or quit, in this case, we use the conditional to print the data again, if the user does not want to see it then the program ends. 
def redo():
    for i in languageData:
        if startOver == "Yes":
            print(languageData)
            break
        elif startOver == "No":
#This is James Gillanders' code
            print("Sorry to hear that! Please run the program again if you would like to continue")
#Calling the function
redo()
        
