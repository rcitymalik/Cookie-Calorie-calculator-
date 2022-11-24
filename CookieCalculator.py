# getting user input
number_of_cookies = input("Please enter how many cookies you ate ?")

#Per serving of 3 cookies nutrition facts
class oreo:
    Calories = 160 # Calories in kcl not calories in gm
    sodium = 190/1000 #converting to gms
    carbohydrates = 25
    fat = 7 #total fat

# per cookie nutrition facts and output of what user has consumed
def total_calories_perCokkie(cookies):
        tcal= (oreo.Calories/3) * float(number_of_cookies)
        tsodium = (oreo.sodium/3) * float(number_of_cookies)
        tcarbs = (oreo.carbohydrates/3) * float(number_of_cookies)
        tfat = (oreo.fat/3)* float(number_of_cookies)

        if tcal > 2000:
            print("You should stop eating these darn delicious cookies") # mandatory output
            print()
            print("Total Calories consumed = ", round(tcal,2), "kcl")
            print("Total sodium consumed = ",round(tsodium,2),"g")
            print("Total fat consumed = " , round(tfat,2),"g")
            print("Total carbohydrates consumed = " , round(tcarbs,2),"g")
        else:
            print("Total Calories consumed = " ,round(tcal,2),"kcl")
            print("Total sodium consumed = " , round(tsodium,2),"g")
            print("Total fat consumed = " ,round(tfat,2),"g")
            print("Total carbohydrates consumed = " , round(tcarbs,2),"g")


# calling the function
total_calories_perCokkie(number_of_cookies)


