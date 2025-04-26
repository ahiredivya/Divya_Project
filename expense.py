from ex import expense

import calendar
import datetime

def main():
    print('Run ho raha hai kya??')
    budget=200000

    expense_file_path = "expense_d.csv"


    expense_chk = check_expense()
    save_file(expense_chk,expense_file_path)
    summerise_expense(expense_file_path,budget)

def check_expense():
    print('kharche ke details de do')
    expense_name=input("Kaha pe kharcha kiya hai :")
    expense_amount=eval(input("Kitna khrcha kiya hai??:"))
    expense_category=["Food","Travelling","Shopping","Work","Fun","Misc"]


    while True:
        print("Konse category mai kharcha kr rhe ho??")
        for i,category_name in enumerate(expense_category):
            print(f"{i+1}.{category_name}")

        value_range=f'[1-{len(expense_category)}]'
        select_index = int(input(f'category bata do : {value_range} : ')) -1

        if select_index in range(len(expense_category)):
            selected_category =expense_category[select_index]
            print(selected_category)

            new_expense = expense(name = expense_name,amt = expense_amount,cat = selected_category)

            return new_expense
            



        else:
            print('Category galat hai')


        break 

    

def save_file(expense_chk:expense,expense_file_path):
    print(f"Kharcha file me save krna hai : {expense_chk} to {expense_file_path}")
    ## It will create the csv file automatically.
    with open (expense_file_path,'a',encoding='utf-8') as f:
        f.write(f'{expense_chk.name},{expense_chk.amount},{expense_chk.category}\n')


def summerise_expense(expense_file_path,budget):
    print("Hum summary bana rahe hai")
    expenses:list[expense]=[]
    with open(expense_file_path,'r',encoding='utf-8') as f :
        lines =f.readlines()
        for line in lines:
            #print(line)
            expense_name,expense_amount,expence_category=line.strip().split(',')
            print(f'{expense_name}   {expense_amount}    {expence_category}')

            line_expense=expense(name=expense_name,amt=float(expense_amount),cat=expence_category)

            expenses.append(line_expense)
            #print(expenses)
    amount_by_category = {}
    for e in expenses:
        key=e.category
        if key in amount_by_category:
            amount_by_category[key]+=e.amount
        else:
            amount_by_category[key]=e.amount
    print("Ye aapka category wise khrcha hai !!!")
    for key,amount in amount_by_category.items():
        print(f'{key}: Rs.{amount:.2f}')   

    total_kharcha =sum([x.amount for x in expenses])
    print(f'Itna khracgha hua hai : Rs.{total_kharcha} /-') 

    remaining_budget= budget - total_kharcha 
    print(f'Itne hi paise bache hai : Rs.{remaining_budget}')   


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]


    remaining_days = days_in_month - now.day

    per_day_budget = remaining_budget/remaining_days

    print(f'Per day kitna kharcha kr sakte ho : Rs.{per_day_budget:.2f} /-')





            
    



if __name__ == "__main__":
    main()




