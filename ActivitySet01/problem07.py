# Strings

text = "X-DSPAM-Confidence:    0.8475"
noIndex=text.find("0.8475")
x=text[noIndex:]
x=float(x)
print(x)
