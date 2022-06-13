# Strings

text = "X-DSPAM-Confidence:    0.8475"
noIndex=text.find(":")
x=text[noIndex+1:]
x=float(x)
print(x)
