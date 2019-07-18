# Define your functions here

# 1. Define a function that returns the string "GET BACK ON YOUR DIET!" if Cookie Monster has eaten any cookies.
#    If he has eaten zero cookies, return the string "Good job, Cookie Monster."

def perfect_day(cookies):
    if  (cookies)>0:
        return "GET BACK ON YOUR DIET!"
    if (cookies)==0:
        return "Good Job Cookie Monster"
print(perfect_day(4))
# 2. Not every day can be a perfect day. Let's write a function for a good_day of dieting.
#    If Cookie Monster has eaten fewer than three cookies, it should return a string that congratulates him.
#    If Cookie Monster has eaten exactly three cookies, let's return a string telling him to stop now.
#    If Cookie Monster has eaten more than three cookies, let's return a string scolding him for eating too many.
def good_day(cookies):
    if (cookies)<3:
        return "Congrants!"
    if (cookies)==3:
        return "STOP NOW!"
    if (cookies)>3:
        return "YOU SHOULD BE ASHAMED OF YOURSELF!"
print(good_day(2))


# 3. The longer Cookie Monster is on this diet, the more we feel we can trust him. Let's write a flex_day function.
#    Let's write a function that takes in two arguments - a goal number of cookies and current number of cookies.
#    It will do the same as the previous function did, so calling flex_day(2, 3) should return a scolding string, since he ate one more than his goal.
def flex_day(goal,current):
    if (current <= goal):
        return "Great You've Reached Your Goal!"
    elif (current>goal):
        return "Oh No, You Passed Your Goal!"
print(flex_day(7,6))


# 4. CHALLENGE: Dieting isn't all about cutting out unhealthy foods; it's also about balance.
#    Let's define a function called balanced_diet that takes in two arguments - a number of cookies and a number of vegetables.
#    If Cookie Monster has eaten more vegetables than he has cookies, congratulate him!
#    If Cookie Monster has eaten the same amount of each, warn him that he should eat a vegetable next.
#    If Cookie Monster has eaten more cookies than vegetables, tell him to get back on his diet. 
#    If Cookie Monster has eaten some vegetables and NO cookies, give him a special congratulations.
#    If Cookie Monster has eaten no vegetables and no cookies, encourage him to eat something - preferrably a vegetable.

def balanced_diet(cookies,vegetables):
    if (cookies<vegetables):
        return "Congrants"
    elif(cookies==vegetables):
        return "You should eat a vegetable next time"
    elif(cookies>vegetables):
        return "Get back on your diet"
    elif(cookies==0,vegetables,>0):
        return "Congrants, you've done more than asked"
    elif