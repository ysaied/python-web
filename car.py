#! /usr/bin/python
from __future__ import division

#input/outputs
txt_original_price = "Honda Civic-LX Sport Retail Price"
txt_rta_registration = "RTA Registration Estimated Fees"
txt_car_insurance = "Car Insurance Estimated Fees"
txt_auto_loan_interest = "Auto Loan Interest Rate"
txt_auto_loan_years = "How many Years Auto Loan (1-5)"
txt_down_payment = "Down Payment"
txt_monthly_installment = "Montly Installment"
txt_total_cost = "Total Paid Amount"
txt_extra_cost = "Extra amount over cash"

print ("\n" * 1)
print ("-" * 60)
original_price = 65000
#original_price = input ("| - " + txt_original_price + (35 - len(txt_original_price)) * " " + "|" + (10 * " ") )
print ("| - " + txt_original_price + (35 - len(txt_original_price)) * " " + "|" + (10 * " ") + str(original_price))

print ("-" * 60)
rta_registration = 630
print ("| - " + txt_rta_registration + (35 - len(txt_rta_registration)) * " " + "|" + (10 * " ") + str(rta_registration))

print ("-" * 60)
car_insurance = 3200
print ("| - " + txt_car_insurance + (35 - len(txt_car_insurance)) * " " + "|" + (10 * " ") + str(car_insurance))

print ("-" * 60)
auto_loan_interest = (3 / 100)
print ("| - " + txt_auto_loan_interest + (35 - len(txt_auto_loan_interest)) * " " + "|" + (10 * " ") + str(auto_loan_interest * 100) + "%")

print ("-" * 60)
auto_loan_years = input ("| - " + txt_auto_loan_years + (35 - len(txt_auto_loan_years)) * " " + "|" + (10 * " "))

print ("-" * 60)
down_payment = input ("| - " + txt_down_payment + (35 - len(txt_down_payment)) * " " + "|" + (10 * " "))

auto_loan_principle = original_price + (rta_registration + car_insurance) - down_payment
auto_loan = auto_loan_principle * (1 + auto_loan_years * auto_loan_interest)

print ("-" * 60)
monthly_installment = round((auto_loan / (auto_loan_years * 12) ))
print ("| - " + txt_monthly_installment + (35 - len(txt_monthly_installment)) * " " + "|" + (10 * " ") + str(monthly_installment))

print ("-" * 60)
total_cost = round(auto_loan + down_payment)
print ("| - " + txt_total_cost + (35 - len(txt_total_cost)) * " " + "|" + (10 * " ") + str(total_cost))

print ("-" * 60)
extra_cost = total_cost - (original_price + car_insurance + rta_registration)
print ("| - " + txt_extra_cost + (35 - len(txt_extra_cost)) * " " + "|" + (10 * " ") + str(extra_cost))

print ("-" * 60)
print ("\n" * 1)