gross_salary = float(input("ხელფასის დაუბეგრავი ოდენობა \n"))
entrepreneurship_status = str(input ("შეიყვანეთ მეწარმეობის სტატუსი:\n 1.ფიზიკური პირი \n 2.მცირე მეწარმე \n 3.შპს \n"))
tax_deduction_18_percent = 18
tax_deduction_1_percent = 1
if entrepreneurship_status == "ფიზიკური პირი" or entrepreneurship_status == "შპს":
    net_salary = gross_salary - ((gross_salary * tax_deduction_18_percent) / 100)
    print ("ხელზე ასაღები ხელფასი =", float(net_salary))
elif entrepreneurship_status == "მცირე მეწარმე":
    net_salary = gross_salary - ((gross_salary * tax_deduction_1_percent) / 100)
    print ("ხელზე ასაღები ხელფასი =", float(net_salary))
else: 
    print ("მეწარმეობის სტატუსი არასწორია")
