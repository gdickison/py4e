# Use find and string slicing to extract the portion of a string after the colon and then use the float function to convert the extracted string into a floating point number

str = "X-DSPAM-Confidence:  0.8475   "
colPos = str.find(":")
numStr = str[colPos+1:]
fStr = float(numStr)
print(fStr)
