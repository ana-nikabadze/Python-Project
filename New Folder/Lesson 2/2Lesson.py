ნაშთი = float(input ("შეიყვანეთ ანგარიშზე არსებული ნაშთის ოდენობა:"))
print ()
გადასახდელი_თანხა = float(input("შეიყვანეთ გადასახდელი თანხის ოდენობა:"))
print ()
საკომისიო = float(input("შეიყვანეთ საკომისიოს ოდენობა:"))
ჯამური_თანხა = float(გადასახდელი_თანხა + საკომისიო)
print ("ჯამურად გადასახდელი თანხა შეადგენს", ჯამური_თანხა, "ლარს")

if (ნაშთი - ჯამური_თანხა) >= 0:
    print ("ტრანზაქცია წარმატებულია")
else: 
    print ("თქვენს ანგარიშზე არ არის საკმარისი თანხა")