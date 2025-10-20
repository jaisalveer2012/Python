age = input ("Please enter your age : ")

age_int = int(age)           #By default input is string, so need to covert to Integer while using with math operaters
if age_int > 20:
    print ("Please go in queue")

elif age_int == 19:
    print ("You are not eligible for driving licence")

else:
    print ("Get Lost")
