# def main():
    
#     # List of string 
#     list1 = ['Hi' ,  'hello', 'at', 'this', 'there', 'from']
    
#     # List of string
#     list2 = ['there' , 'hello', 'Hi']
    
#     '''    
#         check if list1 contains all elements in list2
#     '''
#     result = all(elem in list1  for elem in list2)
#     print (result)
#     if result:
#         print("Yes, list1 contains all elements in list2")    
#     else :
#         print("No, list1 does not contains all elements in list2")    
        
    
#     '''    
#         check if list1 contains any elements of list2
#     '''
#     result =  any(elem in list1  for elem in list2)
    
#     if result:
#         print("Yes, list1 contains any elements of list2")    
#     else :
#         print("No, list1 contains any elements of list2")        
 
        
# if __name__ == '__main__':
#     main()
# #import string
# ## takes in a guess threshold
# ##first we test if guess is valid ,  and penalize if not 
# ##then we test if guess is in word , and penalize if not 
# ## loop until the threshold is hit 
# ##
# guess_threshold = 6
# def is_guess_valid(guess):
#   if len(guess) == 1 and str.isalpha(guess): 
#     return True
#   else:
#     return False

# def user_guess():
#   '''user_guess Takes in no argurments, User Supplies guess input, user_guess Validates Input and
#   returns guess  and  a guess counter increment 

#   Returns:
#       tuple : (guess,  guess increment )
#   '''
#   guess_incr = 0 
#   user_input = ""
#   warning_threshold = 0
#   while is_guess_valid(user_input) != True:
#     user_input = input("Enter your Guess: ")
#     if is_guess_valid (user_input) == False:
#       for warning_counter in range(warning_threshold):
#         warning_counter =+1
#         break 
#       guess_incr += 1
#     if guess_incr >= guess_threshold:
#           user_input = None
#           break
#     print("Guess Number:", guess_incr, "Guess:", user_input)
#   #guess_incr +=1
#   print("Guess Number:", guess_incr, "Guess:", user_input)       
#   return tuple((user_input,guess_incr))
# print(user_guess())
# # def user_guess():
# #   guess_counter= 0
# #   guess = (input("Enter your guess"))
# #   guess_counter = is_guess_valid(guess)
# #   print(guess_counter)
# # def is_guess_valid(guess):
# #   if len(guess) == 1 and str.isalpha(guess): 
# #     return True
# #   else:
# #     for warning_counter in range(3):
# #       warning_counter = +1
# #       print("Please enter a Valid Response",warning_counter," out of 3 warnings before you will be penalized")
# #       return True
# #     return False
# # user_guess()
# # # def game_round():
# # #   print("you ")
# # # def user_guess(guess_amount):
# # #   guessValid = False
# # #   guess_counter= 1
# # #   while guessValid != True:
# # #     guess =(input("Enter your Guess:")).lower()
# # #     print("guess",guess)
# # #     guessValid = is_guess_valid(guess)
# # #     guess_counter= guess_counter_increment(guessValid,guess_counter)
# # #   return guess

# # # def guess_counter_test(guessValid,guess_counter):
# # #   '''user_guess takes in guess counter and increments by 1 if bad   
# # #   Args:
# # #       guess_counter ([type]): [description]
  
# # #   Raises:
# # #       Exception: [description]
  
# # #   Returns:
# # #       [type]: [description]
# # #   '''
# # #   print(guessValid,guess_counter)
# # #   guess_threshold =10
# # #   if guessValid == False:
# # #     guess_counter +=1
# # #     if guess_counter>= guess_threshold:
# # #       raise Exception("Too Many Bad Formatted guesses")
# # #     return guess_counter
# # #   else:
# # #     return guess_counter
# # # def user_guess():
# # #   guess_counter= 0
# # #   guess = (input("Enter your guess"))
# # #   guess_counter = guess_counter_test(is_guess_valid(guess),guess_counter)
# # # def is_guess_valid(guess):
# # #   if len(guess) == 1 and str.isalpha(guess): 
# # #     return True
# # #   else:
# # #     return False

# # def guess_counter_increment(guessValid,guess_counter):x
# #   print(guessValid,guess_counter)
# #   guess_threshold = 
# #   if guessValid == False:
# #     guess_counter +=1
# #     if guess_counter>= guess_threshold:
# #       print("You have run out of guesses :(")
# #       return 
# #     return guess_counter
# #   else:
# #     return guess_counter