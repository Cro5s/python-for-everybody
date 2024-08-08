'''
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
'''

def compute_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        base_pay = (hours - overtime_hours) * rate
        overtime_pay = overtime_hours * overtime_rate
        
        return base_pay + overtime_pay
    else:
        return hours * rate

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
gross_pay = compute_pay(hours, rate)

print('Pay', gross_pay)