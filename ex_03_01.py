def computePay(hours, rate):
    if hours > 40:
        ot = hours - 40
        pay = rate*40 + rate*ot*1.5
    else:
        pay = rate*hours
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
computePay(h,r)
print(pay)
