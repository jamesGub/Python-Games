#CINF 308 Assignment 9 -  Inheritance
#This is James Gillanders' code

#On the theme of revising programs, we will be demonstrating inheritance while changing the functionality of our program significantly.
#Inheritance is a core concept in OOP, so its understanding is useful to grasp. Our program will be in the style of a software update
#for a smartphone, pulling from some actual iOS update documentation to make it sound more authentic.

#Need to import our class from an external file. 


from software_version1 import Software_Version1
    
#Here we are calling each of our functions with our new object. But as the last line states, updates are being added
#so we will create a new class that includes these features plus the ones from before. 

mySmartPhone = Software_Version1()
mySmartPhone.features()
mySmartPhone.OS()
mySmartPhone.version()
mySmartPhone.new_features()


#After importing our new software version file, we can call on the new functions while retaining the old ones
#even though we "removed the functions" and moved them to the new class. Basically, we inherited them.
    
  





