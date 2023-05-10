# mortgage.py
#
# Exercise 1.7

from tkinter import ROUND


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        if principal < payment + extra_payment:
            total_paid = round(total_paid + principal, 2)
            principal = 0
            months = months + 1
        else: 
            principal = round(principal * (1+rate/12) - payment - extra_payment, 2)
            total_paid = round(total_paid + payment + extra_payment, 2)
            months = months + 1
    else:
        if principal < payment:
            total_paid = round(total_paid + principal, 2)
            principal = 0 
            months = months +1
        else:
            principal = round(principal * (1+rate/12) - payment, 2)
            total_paid = round(total_paid + payment, 2)
            months = months + 1
    print(months, total_paid, principal)

print('Total paid', total_paid)
print('Total months', months)
~