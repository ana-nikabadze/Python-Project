
# დაწერეთ პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. 
# შექმენით საწყისი ცვლადი total_sum =0, შეამოწმეთ რიცხვი
# თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. 
# ესპროცესი გაგრძელდეს იქამდე სანამ
# მომხმარებელი არ შეიყვანს'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

total_sum = 0
active_process = True
import random
while active_process == True:
    random_num = random.randint(-10, 10)
    print (random_num)
    if random_num >= 0:
        total_sum = (total_sum + random_num)
    else:
        print ("რიცხვი უარყოფითია, შეკრების ოპერაცია არ შესრულდა")
        
    user_response = input("ჯამის სანახავად ჩაწერეთ sum\n")
    if user_response == "sum":
        active_process = False
        print ("შეყვანილი დადებითი რიცხვების ჯამია", total_sum) 

