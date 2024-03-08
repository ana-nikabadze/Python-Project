size = str(input ("მიუთითეთ ზომა\n"))
check_small = "small"
check_tall = "tall"
check_middle = "middle"
if check_small in size:
    print (f"{check_small} არის ტექსტში")
elif check_tall in size:
    print (f"{check_tall} არის ტექსტში")
elif check_middle in size:
    print (f"{check_middle} არის ტექსტში")
else:
    print("სიტყვა ვერ მოიძებნა")
    
# ირაკლი, პირობაში ეწერა რომ პირველივე სიტყვა დაბეჭდეო და ეგ ვერ გავაკეთე. 
# მაგალითად რომ შევიყვანო middle tall small, რადგან პირველი მიდევს small შემოწმება
# small გამოაქვს პირველი. მოკლედ ეგ ვერ გავიხსენე. 