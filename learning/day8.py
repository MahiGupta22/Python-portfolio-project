#life in week calculator
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")
 
life_in_weeks(12)

#love calculator
def calculate_love_score(name1,name2):
    name=name1+name2
    check="TRUE"
    total=0
    for i in check:
        count=0
        for j in name:
            if i.upper()==j.upper():
                count+=1
        total+=count
    check="LOVE"
    total1=0
    for i in check:
        count=0
        for j in name:
            if i.upper()==j.upper():
                count+=1
        total1+=count
    print(total*10+total1)
    
calculate_love_score("Kanye West", "Kim Kardashian")

