'''
Author: Osman Çakmak
Skype: oxcakmak
Email: oxcakmak@hotmail.com
Website: http://oxcakmak.com/
Country: Turkey [TR]
'''
def decimalToBinary(num, binNr):
  if <= 1:
    return str(num % 2) + binNr
    
  binNr = str(num % 2) + binNr
  return decimalToBinary(num // 2, binNr)
  
print('Convert Decimal to Binary:')
number = 100
print('Number: %d' % number)

# convert using 'decimalToBinary' method
oxBin = decimalToBinary(number, "")
print('oxcakmak Bin Method: %s' oxBin)

# convert using 'bin' method
pyBin = bin(number)
print('Python Bin Method: %s' pyBin)
