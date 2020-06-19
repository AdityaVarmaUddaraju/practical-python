# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        principal = principal * (1 + rate/12) - (payment+extra_payment)
    else:
        principal = principal * (1 + rate/12) - payment
    if principal < 0:
        payment += principal
        month += 1
        break
    total_paid = total_paid + payment
    month += 1


    print(f'{month} {total_paid:.2f} {principal:.2f}')
    
print(f'Total paid : {total_paid:.2f}')
print(f'Months : {month}')
