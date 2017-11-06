def computepay(hours, rate):
    h = float(hours)
    r = float(rate)
    if h > 40:
        ot = h - 40
        pay = r*40 + r*ot*1.5
    else:
        pay = r*h
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate:")
print(computepay(hours, rate))
